package db

@Grab('mysql:mysql-connector-java:5.1.25')
@GrabConfig(systemClassLoader = true)
import groovy.sql.Sql

class Database {
    private def db
    private def sql
    private def config

    def connect() {
        db = [url: "jdbc:mysql://$config.host/$config.database?useUnicode=true&characterEncoding=UTF-8",
                  user: config.username, password: config.password, driver: 'com.mysql.jdbc.Driver']

        sql = Sql.newInstance(db.url, db.user, db.password, db.driver)
    }

    def close() {
        sql.close()
        println "Database connection terminated"
    }

    def getAllRows(String table) {
        String query = "SELECT * from ${table}"

        sql.rows(query);
    }

    def executeUpdate(String query) {
        sql.executeUpdate query
    }
}
