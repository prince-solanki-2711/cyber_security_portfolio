# TryHackMe – Data Representation

## Lab Completion Proof

![TryHackMe Data Representation Completion](screenshot/room-completed.png)

*Screenshot showing completion of the Data Representation room on TryHackMe.*

## Overview

I completed the **Data Representation** room in the Pre Security learning path on TryHackMe.

This lab introduced me to how computers represent data using binary digits, how decimal, binary, and hexadecimal number systems work, and how computers represent colors using hexadecimal values.

## What I Learned

### 1. Introduction to Data Representation
- Learned how computers represent and store different types of data.
- Understood that computers use binary digits, `0` and `1`, to represent information.
- Learned that numbers, colors, and other data can be represented using different formats.

### 2. Our First Eight Colors
- Learned how binary values can represent a limited number of colors.
- Understood that using a small number of bits limits how many different values can be represented.
- Explored the basic idea of representing colors using binary combinations.

### 3. From 8 to 16 Million Colors
- Learned how increasing the number of bits available for color representation allows computers to display more colors.
- Understood that RGB color representation commonly uses three color channels: Red, Green, and Blue.
- Learned that using 8 bits for each RGB channel allows \(256\) possible values per channel, resulting in \(256 \times 256 \times 256 = 16,777,216\) possible color combinations.

### 4. Hexadecimal Representation
- Learned that hexadecimal is a base-16 number system.
- Understood that hexadecimal uses the digits `0–9` and the letters `A–F`.
- Learned that one hexadecimal digit represents four binary bits, making hexadecimal a more compact way to write binary values.

### 5. Representing Colors in Hexadecimal
- Learned how hexadecimal values are used to represent colors.
- Understood that a common RGB hexadecimal color code contains six digits, with two hexadecimal digits representing each color channel.
- Learned how the red, green, and blue components combine to produce a particular color.

For example, `#FF0000` represents red, `#00FF00` represents green, and `#0000FF` represents blue.

### 6. How Computers Represent Data
- Learned that computers use binary because their underlying digital circuits can represent two distinct states.
- Understood that combinations of bits can represent numbers and other types of information.
- Learned that different data formats provide different ways to interpret the same underlying binary values.

### 7. Decimal Number System
- Learned that decimal is a base-10 number system.
- Understood that it uses ten digits: `0–9`.
- Learned that each digit's position represents a power of 10.

### 8. Binary Number System
- Learned that binary is a base-2 number system.
- Understood that it uses only two digits: `0` and `1`.
- Learned that each binary digit represents a power of 2 according to its position.

### 9. Hexadecimal Number System
- Learned that hexadecimal is a base-16 number system.
- Understood how hexadecimal values relate to binary values.
- Learned that hexadecimal is useful for representing binary data in a shorter, more readable form.

## Practical Experience

During this lab, I explored how computers represent numbers and colors using different number systems.

I learned how binary values represent data, how the decimal, binary, and hexadecimal number systems differ, and how hexadecimal color codes represent RGB color components.

## SOC Analyst Relevance

Understanding data representation provides a foundation for learning how computers store and process information.

This knowledge is useful for a SOC Analyst because:
- Binary is fundamental to understanding how digital systems represent data.
- Hexadecimal is commonly encountered when examining memory addresses, file data, and technical security information.
- Understanding number systems helps when interpreting low-level technical data.
- Learning how data is represented supports further study of networking, digital forensics, and cybersecurity fundamentals.

As I continue preparing for a SOC Analyst Level 1 role, I will build on these fundamentals while learning how data is represented in network traffic, files, and security-related technical outputs.

## Key Takeaways

- Computers represent information using binary digits, `0` and `1`.
- Decimal uses base 10, binary uses base 2, and hexadecimal uses base 16.
- Hexadecimal uses the digits `0–9` and letters `A–F`.
- One hexadecimal digit represents four binary bits.
- RGB uses red, green, and blue components to represent colors.
- Using 8 bits per RGB channel allows 16,777,216 possible color combinations.
- Understanding number systems is a useful foundation for computer science and cybersecurity.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Pre Security
- **Room:** Data Representation
- **Topics:** Binary, decimal, hexadecimal, and color representation
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.
