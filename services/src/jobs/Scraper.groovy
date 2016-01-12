package jobs

import db.Configuration
import db.Database
import interests.Interest

class Scraper {
    static void main(String[] args) {
        Configuration config = new Configuration()

        Database db = new Database(config: config)
        db.connect()
        def interests = []

        db.getAllRows("Interest").each { row ->
            def interest = new Interest(keyword: row.keyword, link: row.link, lastUpdated: row.last_updated, db: db)
            interests.add(interest)
        }

        interests.each { row ->
            row.updateLink()
        }

        db.close()
    }
}
