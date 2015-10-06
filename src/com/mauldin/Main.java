package com.mauldin;

import com.mauldin.db.Database;
import com.mauldin.subscribers.Subscriber;

public class Main {

    public static void main(String[] args) {
        Subscriber subscriber = new Subscriber("Peter", "Mauldin", "petermauldin@utexas.edu");

//        subscriber.printSubscriberInfo();

        Database db = new Database();
        int connected = db.connect("one_a_day");
        if(connected == 0) {
            db.viewSubscribers();

            db.close();
        }
    }
}
