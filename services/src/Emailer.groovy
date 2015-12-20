import db.Configuration
import db.Database
import subscribers.Subscriber

class Emailer {
    static void main(String[] args) {
        Configuration config = new Configuration()

        Database db = new Database(config: config)
        db.connect()

        def subscribers = []

        db.getAllRows("Subscriber").each { row ->
            def subscriber = new Subscriber(row.user_id, row.subscriberid,
                    row.last_emailed, row.frequency, db)
            subscribers.add(subscriber)
        }
    }
}
