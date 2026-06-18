# Assignment 5: GUI Designing and Event Handling

## Problem Statement / Aim
To design a basic Graphical User Interface and handle user events using Java Swing.

## Theory & Concept
**Java Swing** is a lightweight GUI toolkit that includes components like `JFrame`, `JButton`, `JLabel`, and `JTextField`.

**Event Handling** allows a program to respond to user actions (like button clicks). It requires a source object, an event object, and an event listener interface (e.g., `ActionListener`).

## Fully Solved Code
```java
import javax.swing.*;
import java.awt.event.*;

public class ClickCounter {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Click Counter");
        JButton button = new JButton("Click Me");
        JLabel label = new JLabel("Clicks: 0");

        button.setBounds(50, 50, 100, 30);
        label.setBounds(60, 90, 100, 30);

        final int[] count = {0};

        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                count[0]++;
                label.setText("Clicks: " + count[0]);
            }
        });

        frame.add(button);
        frame.add(label);
        frame.setSize(250, 200);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
```

## Expected Output
```
[A window pops up with a "Click Me" button. Clicking the button increments the "Clicks: 0" counter.]
```

---
[[CS-306-Viva-5|View Viva Questions]]
