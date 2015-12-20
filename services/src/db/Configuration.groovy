package db

import groovy.json.JsonSlurper

class Configuration {
    def username
    def host
    def database
    def password

    def sendgrid_username
    def sendgrid_password

    def Configuration() {
        File configFile = new File('src/config.json')

        def jsonSlurper = new JsonSlurper()
        def config = jsonSlurper.parse(configFile)

        def db_config = config["db"]

        username = db_config["username"]
        host = db_config["host"]
        database = db_config["database"]
        password = db_config["password"]

        def sendgrid_config = config["sendgrid"]

        sendgrid_username = sendgrid_config["username"]
        sendgrid_password = sendgrid_config["password"]
    }
}
