# TryHackMe – How Websites Work

## Lab Completion Proof

![TryHackMe How Websites Work Completion](screenshot/room-completed.png)

*Screenshot showing completion of the How Websites Work room on TryHackMe.*

## Overview

I completed the **How Websites Work** room in the Pre Security learning path on TryHackMe.

This lab introduced me to how websites work and how web browsers communicate with web servers. I learned about the frontend and backend components of a website, the technologies used to create websites, HTML, JavaScript, and how different HTML elements work.

I also learned about sensitive data exposure and HTML injection, including how these vulnerabilities occur and how they can be prevented.

## What I Learned

### 1. Introduction to How Websites Work

- Learned the basic working of websites.
- Understood how a web browser communicates with a web server.
- Learned how different technologies work together to create and display websites.
- Understood the role of frontend and backend components in website development.

### 2. What Is a Web Server?

- Learned that a web server is a system that stores, processes, and delivers website content to users.
- Understood how a web server receives requests from a browser and sends responses back.
- Learned that web servers help users access websites through the Internet.

### 3. Two Major Components of a Website

Learned that a website has two major components: frontend and backend.

**Frontend:**
- Understood that the frontend is the part of a website that users can see and interact with.
- Learned that it includes elements such as text, images, buttons, forms, and menus.
- Understood that HTML, CSS, and JavaScript are commonly used to build the frontend.

**Backend:**
- Learned that the backend handles the operations that happen behind the scenes.
- Understood that it processes requests, handles data, and communicates with databases.
- Learned that users do not directly see the backend operations.

### 4. How Does a Website Work?

- Learned how a website loads when a user enters its address into a browser.
- Understood that the browser sends a request to the web server.
- Learned that the server processes the request and sends the required website files back to the browser.
- Understood how the browser uses these files to display the website.
- Learned how the frontend and backend work together to provide website functionality.

### 5. Technologies Used to Create Websites

- Learned about the different technologies used in website development.
- Understood that different technologies have different purposes.
- Learned how HTML, CSS, JavaScript, and backend technologies work together to create websites.

### 6. Purpose of Different Website Technologies

| Technology | Purpose |
|---|---|
| HTML | Defines the structure and content of a webpage. |
| CSS | Controls the appearance and design of a webpage. |
| JavaScript | Adds functionality and interactive features to a webpage. |
| Backend Technologies | Handle server-side operations and process requests. |
| Databases | Store and manage website information. |

### 7. What Is HTML?

- Learned that HTML stands for HyperText Markup Language.
- Understood that HTML is used to create the structure of a webpage.
- Learned how HTML defines different elements such as headings, paragraphs, images, and links.
- Understood that browsers read HTML documents and display their content as webpages.

### 8. Basic Structure of an HTML Document

- Learned about the basic structure of an HTML document.
- Understood how different HTML elements are arranged to create a webpage.
- Learned the purpose of important HTML elements such as `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>`, and `<body>`.
- Understood that the `<head>` section contains information about the webpage, while the `<body>` section contains the content displayed to users.

### 9. HTML Tags and Their Purpose

- Learned that HTML tags are used to define different elements on a webpage.
- Understood how tags tell the browser what type of content to display.
- Learned about commonly used HTML tags and their purposes.

| HTML Tag | Purpose |
|---|---|
| `<html>` | Defines the root of an HTML document. |
| `<head>` | Contains information about the webpage. |
| `<title>` | Sets the title of the webpage. |
| `<body>` | Contains the visible content of the webpage. |
| `<h1>` | Defines a main heading. |
| `<p>` | Defines a paragraph. |
| `<img>` | Displays an image. |
| `<a>` | Creates a hyperlink. |

### 10. HTML Attributes

- Learned that HTML attributes provide additional information about HTML elements.
- Understood that attributes are written inside the opening tag of an HTML element.
- Learned that attributes usually contain a name and a value.
- Understood how attributes can change the behaviour or provide additional details about an element.

### 11. Class Attribute

- Learned that the `class` attribute is used to identify and group HTML elements.
- Understood that the same class name can be assigned to multiple elements.
- Learned that classes are commonly used to apply CSS styling or select elements using JavaScript.

### 12. Src Attribute

- Learned that the `src` attribute specifies the location of an external resource.
- Understood that it is commonly used with elements such as `<img>` and `<script>`.
- Learned how the browser uses the specified source to load an image or an external JavaScript file.

### 13. Multiple Attributes

- Learned that an HTML element can contain multiple attributes.
- Understood that each attribute provides different information about the element.
- Learned that multiple attributes can be written inside the same opening HTML tag.

### 14. ID Attribute

- Learned that the `id` attribute is used to identify a specific HTML element.
- Understood that an ID should be unique within a webpage.
- Learned that IDs can be used to apply CSS styling or select specific elements using JavaScript.
- Understood the difference between the `class` and `id` attributes.

## JavaScript

### 15. What Is JavaScript?

- Learned that JavaScript is a programming language used in website development.
- Understood that JavaScript adds functionality and interactive features to webpages.
- Learned how JavaScript works alongside HTML and CSS.
- Understood that JavaScript allows webpages to respond to user actions.

### 16. Why Is JavaScript Used?

- Learned why JavaScript is important in website development.
- Understood that it makes webpages more interactive and dynamic.
- Learned how JavaScript can respond to user actions, update webpage content, and perform different operations.
- Understood how JavaScript helps improve the functionality of a website.

### 17. How Is JavaScript Added to a Website?

- Learned that JavaScript can be added directly inside an HTML document using the `<script>` tag.
- Understood that JavaScript can also be added through an external JavaScript file.
- Learned how the `src` attribute is used to link an external JavaScript file to an HTML document.
- Understood how the browser loads and executes JavaScript code.

## Website Vulnerabilities

### 18. What Is Sensitive Data Exposure?

- Learned that sensitive data exposure occurs when important or private information is accessible to people who should not have access to it.
- Understood that websites may accidentally expose sensitive information through their frontend or other accessible resources.
- Learned why protecting sensitive information is important for website security.

### 19. How Does Sensitive Data Exposure Occur?

- Learned that sensitive information can be exposed when developers accidentally include private information in publicly accessible website content.
- Understood that information may be exposed through HTML source code, comments, or other resources available to users.
- Learned that information intended to remain private should not be included in publicly accessible frontend code.

### 20. Why Is Sensitive Data Exposure Dangerous?

- Learned that exposed sensitive information can be accessed by unauthorised users.
- Understood that attackers may use exposed information to gain further access or identify weaknesses in a website.
- Learned that sensitive data exposure can put user information and website security at risk.

### 21. How to Identify Sensitive Data Exposure

- Learned how to inspect a webpage to identify information that should not be publicly accessible.
- Understood how viewing the page source can help identify exposed information.
- Learned that HTML source code may contain information that is not directly visible on the webpage.
- Understood why checking publicly accessible website content is important when identifying sensitive data exposure.

### 22. What Is HTML Injection?

- Learned that HTML injection is a vulnerability that occurs when unfiltered user input is displayed on a webpage.
- Understood that an attacker can inject HTML code into a vulnerable website when user input is not properly sanitised.
- Learned that the injected HTML code may be interpreted and displayed by the browser.
- Understood why handling user input properly is important for website security.

### 23. What Is Input Sanitisation?

- Learned that input sanitisation means filtering or cleaning user input before it is used by a website.
- Understood that sanitisation helps prevent unwanted or malicious content from being processed or displayed.
- Learned why websites should not blindly trust information entered by users.
- Understood that proper input handling helps reduce HTML injection vulnerabilities.

### 24. HTML Injection Is a Client-Side Vulnerability

- Learned that HTML injection affects how a webpage is displayed in the user's browser.
- Understood that injected HTML can change the content or appearance of a webpage.
- Learned that the browser interprets the injected HTML when vulnerable user input is included in the page.
- Understood why HTML injection is considered a client-side vulnerability.

### 25. How Does HTML Injection Work?

- Learned how HTML injection occurs when a website accepts user input without properly sanitising it.
- Understood that the website uses the supplied input in its webpage content.
- Learned that if the input contains HTML code, the browser may interpret it as actual HTML instead of displaying it as normal text.
- Understood how an attacker can use this weakness to modify the content displayed on a webpage.

### 26. How to Prevent HTML Injection?

- Learned that proper input sanitisation is important for preventing HTML injection.
- Understood that websites should filter or sanitise user input before displaying it.
- Learned why user-provided content should be handled carefully.
- Understood that preventing untrusted input from being interpreted as HTML helps protect webpages from injection attacks.

### 27. HTML Injection and Database Injection

- Learned that HTML injection and database injection are different types of injection vulnerabilities.
- Understood that HTML injection involves injecting HTML code into a webpage through unfiltered user input.
- Learned that database injection involves injecting malicious input into database queries.
- Understood that both vulnerabilities can occur when applications do not properly handle user input.
- Learned why proper input handling is important for protecting websites and their data.

## Practical Experience

During this lab, I learned how websites work and explored different technologies and vulnerabilities related to web applications.

While exploring the different topics, I gained hands-on experience and understanding of:

- Understanding how browsers communicate with web servers.
- Identifying the frontend and backend components of a website.
- Learning about HTML, CSS, and JavaScript.
- Understanding the basic structure of an HTML document.
- Working with HTML tags and attributes.
- Understanding how JavaScript is added to a webpage.
- Identifying sensitive information exposed through website content.
- Understanding how HTML injection vulnerabilities occur.
- Learning the importance of input sanitisation.
- Understanding the difference between HTML injection and database injection.

This lab helped me understand how websites are built, how they work, and some common security issues that can affect web applications.

## SOC Analyst Relevance

Understanding how websites work is useful for a SOC Analyst because web applications are commonly involved in security incidents and attacks.

The concepts learned in this lab provide a foundation for:

- Understanding how web browsers and servers communicate.
- Identifying sensitive information exposed through publicly accessible website content.
- Understanding how attackers may exploit weaknesses in web applications.
- Recognising HTML injection vulnerabilities.
- Understanding why improper input handling can create security risks.
- Differentiating between client-side injection and database injection vulnerabilities.
- Understanding the importance of secure web application development.

As I continue preparing for a SOC Analyst Level 1 role, this knowledge will help me understand web application vulnerabilities and recognise suspicious activities involving websites.

## Key Takeaways

- Websites mainly consist of frontend and backend components.
- A web server receives requests and sends website content to browsers.
- HTML defines the structure of a webpage.
- CSS controls the appearance of a webpage.
- JavaScript adds functionality and interactive features.
- HTML tags define different webpage elements.
- HTML attributes provide additional information about elements.
- Sensitive data exposure occurs when private information becomes accessible to unauthorised users.
- HTML injection occurs when unfiltered user input is interpreted as HTML by the browser.
- Input sanitisation helps prevent HTML injection.
- HTML injection and database injection are different types of injection vulnerabilities.
- Understanding website technologies and vulnerabilities is useful for cybersecurity and SOC investigations.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Pre Security
- **Room:** How Websites Work
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.