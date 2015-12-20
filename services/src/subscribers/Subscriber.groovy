package subscribers

class Subscriber {
    String firstName, lastName, email;

    def Subscriber(String firstName, String lastName, String email) {
        this.firstName = firstName
        this.lastName = lastName
        this.email = email
    }

    def printSubscriberInfo() {
        println "Subscriber Information\nName: ${firstName} ${lastName}\nEmail Address: ${email}\n"
    }
}
