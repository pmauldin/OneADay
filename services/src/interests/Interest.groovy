package interests

import db.Database

class Interest {
    def keyword
    def link
    def lastUpdated

    String toString() {
        "Keyword: ${keyword}\tLink: ${link}\tLast Updated: ${lastUpdated}"
    }

}
