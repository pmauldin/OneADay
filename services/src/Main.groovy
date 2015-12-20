import db.Database
import subscribers.Subscriber

class Main {
    static void main(String[] args) {
//        Subscriber subscriber = new Subscriber("Peter", "Mauldin", "petermauldin@utexas.edu")

//        subscriber.printSubscriberInfo()

        Database db = new Database()
        db.connect "admin", "159.203.64.72:3306", "one_a_day", "Orangebox1"
        db.viewSubscribers()

        db.close()
    }
}
