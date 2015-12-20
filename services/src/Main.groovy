import db.Database
import interests.Interest

class Main {
    static void main(String[] args) {
        Database db = new Database()
        db.connect "admin", "159.203.64.72:3306", "one_a_day", "Orangebox1"
        def interests = db.getAllRows("Interest")

        interests.each ({ row ->
            def interest = new Interest(keyword: row.keyword, link: row.link, lastUpdated: row.last_updated)
            println interest
//            println interest
//            println interest.getClass()
        })

        db.close()
    }
}
