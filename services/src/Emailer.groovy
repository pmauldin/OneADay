import com.sendgrid.SendGrid
import db.Configuration
import db.Database
import subscribers.Subscriber

class Emailer {
    private static SendGrid sendgrid

    static void main(String[] args) {
        Configuration config = new Configuration()
        sendgrid = new SendGrid(config.sendgrid_username, config.sendgrid_password)

        Database db = new Database(config: config)
        db.connect()

        db.getAllRows("Subscriber").each { row ->
            def subscriber = new Subscriber(row.user_id, row.subscriberid,
                    row.last_emailed, row.frequency, db)
            sendEmail(subscriber)
        }
    }

    static sendEmail(Subscriber subscriber) {
        if (subscriber.interests.size() == 0) {
            return
        }

        println subscriber.interests

        def html = """<!DOCTYPE html>
                    <html>
                    <body>
                    <h2>Here are the top results for your interests in the last 24 hours:</h2>
                    """

        subscriber.interests.forEach { interest ->
            html += """<h4 style="margin:0"><a href="$interest.link">$interest.keyword</a></h4><br>"""
        }

        SendGrid.Email email = new SendGrid.Email()
        email.addTo(subscriber.email.toString())
        email.setFrom("admin@oneaday.com")
        email.setSubject("OneADay Newsletter")

        html += """</body>
                    </html>"""

        email.setHtml(html)

        sendgrid.send(email)
    }
}
