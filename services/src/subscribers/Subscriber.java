package subscribers;

public class Subscriber {
    String firstName, lastName, email;

    public Subscriber(String firstName, String lastName, String email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }

    public void printSubscriberInfo() {
        System.out.printf("Subscriber Information\nName: %s %s\nEmail Address: %s\n", firstName, lastName, email);
    }
}
