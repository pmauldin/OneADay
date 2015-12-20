package db

@Grab('mysql:mysql-connector-java:5.1.25')
@GrabConfig(systemClassLoader = true)
import groovy.sql.Sql

class Database {
    private def db
    private def sql

    def connect(String username, String host, String database, String password) {
        db = [url: "jdbc:mysql://$host/$database?useUnicode=true&characterEncoding=UTF-8",
                  user: username, password: password, driver: 'com.mysql.jdbc.Driver']

        sql = Sql.newInstance(db.url, db.user, db.password, db.driver)
    }

    def close() {
        sql.close()
        println "Database connection terminated"
    }

    def viewSubscribers(){
        String query = "SELECT * from Subscriber"

        sql.eachRow(query, {
            subscriber -> println subscriber
        })
    }
}
