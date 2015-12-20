package db

import groovy.json.JsonSlurper

class Configuration {
    def username
    def host
    def database
    def password

    def Configuration() {
        File configFile = new File('src/db/config.json')

        def jsonSlurper = new JsonSlurper()
        def config = jsonSlurper.parse(configFile)["db"]

        username = config["username"]
        host = config["host"]
        database = config["database"]
        password = config["password"]
    }
}
