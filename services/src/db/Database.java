package db;

import java.sql.*;

public class Database {
    private Connection conn = null;

    public int connect(String name) {
        String username = "admin";
        String hostname = "159.203.64.72:3306";
        String password = "pu8REmap!$wu3H";

        try {
            Class.forName ("com.mysql.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://" + hostname + "/" + name, username, password);
            System.out.println("Database connection established");
        } catch (Exception e) {
            e.printStackTrace();
            return 1;
        }
        return 0;
    }

    public int close() {
        if(conn != null) {
            try {
                conn.close();
                System.out.println("Database connection terminated");
                return 0;
            } catch (Exception e) {
                e.printStackTrace();
                return 1;
            }
        } else {
            return 2;
        }
    }

    public void viewSubscribers(){
        Statement stmt = null;
        String query = "SELECT * from Subscriber";

        try {
            stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            ResultSetMetaData rsmd = rs.getMetaData();
            int columnsNumber = rsmd.getColumnCount();
            while (rs.next()) {
                for (int i = 1; i <= columnsNumber; i++) {
                    if (i > 1) System.out.print(",  ");
                    String columnValue = rs.getString(i);
                    System.out.print(rsmd.getColumnName(i) + ": " + columnValue);
                }
                System.out.println("");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
