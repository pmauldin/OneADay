package interests

@Grab('org.jsoup:jsoup:1.7.1')
import groovy.json.StringEscapeUtils

import java.text.SimpleDateFormat

class Interest {
    def seu
    def keyword
    def link
    def lastUpdated
    def db

    def Interest() {
        seu = new StringEscapeUtils()
    }

    def updateLink() {
        def now = new Date()

        if (!keyword) {
            println "Skipping update, keyword undefined..."
            return
        }

//        if (lastUpdated != null) {
//            //in milliseconds
//            def diff = now.getTime() - lastUpdated.getTime();
//
//            def diffSeconds = diff / 1000 % 60;
//            print diffSeconds
//        }

        def query = seu.escapeJavaScript(keyword).replaceAll(" ", "+") + "&tbas=0&tbm=nws&tbs=qdr:d"

        def html = org.jsoup.Jsoup
                .connect("http://www.google.com/search?q=" + query)
                .userAgent("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0")
                .get().select("h3.r > a").attr("href")

        link = html.substring(html.indexOf("=") + 1, html.length())

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        lastUpdated = sdf.format now

        updateInterestRow()
    }

    def updateInterestRow() {
        def query = "UPDATE Interest set link='${link}',last_updated='${lastUpdated}' where keyword='${keyword}'"
        db.executeUpdate(query)
        println "Updated $keyword"
    }

    String toString() {
        "Keyword: ${keyword}\tLink: ${link}\tLast Updated: ${lastUpdated}"
    }

}
