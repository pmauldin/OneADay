package subscribers

import interests.Interest

class Subscriber {
    def user_id
    def sub_id
    def username
    def email
    def last_emailed
    def frequency
    def db
    def interests

    def Subscriber(id, sid, last_email, freq, conn) {
        user_id = id
        sub_id = sid
        db = conn
        last_emailed = last_email
        frequency = freq
        populateUserInfo()
        getInterests()
    }

    def populateUserInfo() {
        def info = db.getRowsConditional("auth_user", "id=$user_id")[0]

        username = info.username
        email = info.email
    }

    def getInterests() {
        def interestList = []
        def interest_ids = db.getRowsConditional("Subscriber_keywords", "subscriber_id=$sub_id")
        interest_ids.each { row ->
            def interestRow = db.getRowsConditional("Interest", "keyword='$row.interest_id'")
            def interest = new Interest(keyword: interestRow.keyword[0], link: interestRow.link[0],
                                        lastUpdated: interestRow.last_updated[0], db: db)
            interestList.add(interest)
        }

        interests = interestList
    }

    String toString() {
        "UserID: $user_id   SubscriberID: $sub_id   Username: $username   " +
                "Email: $email   Last Email: $last_emailed   Frequency $frequency"
    }
}
