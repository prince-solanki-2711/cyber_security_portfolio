# TryHackMe – Data Encoding

## Lab Completion Proof

![TryHackMe Data Encoding Completion](screenshot/room-completed.png)

*Screenshot showing completion of the Data Encoding room on TryHackMe.*

## Overview

I completed the **Data Encoding** room in the Pre Security learning path on TryHackMe.

This lab introduced me to how computers represent text, the difference between representation and encoding, ASCII, the limitations of ASCII, and Unicode encoding formats such as UTF-8, UTF-16, and UTF-32.

## What I Learned

### 1. How Computers Represent Text
- Learned how computers represent text using numerical values.
- Understood that letters, numbers, and symbols need a defined representation so computers can store and process them.
- Learned that text can be encoded into bytes for storage and transmission.

### 2. Representation and Encoding
- Learned the difference between representing a character and encoding it into bytes.
- Understood that a character set defines which characters are available and their associated code points.
- Learned that a character encoding defines how those code points are converted into bytes.

### 3. Weird or Gibberish Characters
- Learned why text may appear as strange or unreadable characters when it is decoded using the wrong encoding.
- Understood that encoding mismatches can occur when the sender and receiver interpret the same bytes differently.
- Recognized that selecting the correct encoding is important for displaying text properly.

### 4. What Is ASCII?
- Learned that ASCII stands for **American Standard Code for Information Interchange**.
- Understood that standard ASCII uses 7 bits to represent 128 characters.
- Learned that it includes English letters, digits, punctuation marks, and control characters.

### 5. ASCII Examples
- Learned that each standard ASCII character has a numerical value.
- Understood that these values can be represented in decimal, binary, or hexadecimal.
- Learned that the same character can be represented differently depending on the number system used.

### 6. Representing "TryHackMe" in ASCII
- Learned how the characters in `TryHackMe` correspond to individual ASCII values.
- Understood that text can be converted into numerical values and then represented in binary or hexadecimal.
- Recognized that text encoding allows computers to store and transmit written information as bytes.

### 7. ASCII and European Languages
- Learned that standard ASCII does not include many characters used in European languages, such as `ñ` and `ü`.
- Understood that extended character encodings were introduced to support additional characters.
- Learned that different extended encodings could assign different meanings to the same byte value, creating compatibility problems.

### 8. Encoding Mismatch
- Learned that an encoding mismatch occurs when text is interpreted using an encoding different from the one used to encode it.
- Understood that this can cause readable text to appear as gibberish or unexpected symbols.
- Recognized the importance of using compatible encodings when exchanging text between systems.

### 9. Limitations of ASCII
- Learned that standard ASCII supports only 128 character values.
- Understood that its limited character set cannot represent the many writing systems and symbols used worldwide.
- Learned why a more universal approach to text representation was needed.

### 10. Why Unicode Is Needed
- Learned that Unicode provides a standard system for assigning code points to characters from many writing systems.
- Understood that Unicode supports characters from languages around the world, along with many symbols.
- Learned that Unicode helps improve text compatibility across different platforms and applications.

### 11. Unicode Example
- Learned that Unicode can represent characters that are not available in standard ASCII.
- Understood that characters such as `ñ`, `€`, `あ`, and `ب` can be represented using Unicode code points.
- Recognized the importance of Unicode for multilingual text processing.

### 12. UTF-8, UTF-16, and UTF-32
- Learned that UTF stands for **Unicode Transformation Format**.
- Understood that UTF-8, UTF-16, and UTF-32 are different ways of encoding Unicode code points.
- Learned the basic differences between these formats:
  - **UTF-8:** Uses one to four bytes per Unicode code point and is compatible with standard ASCII.
  - **UTF-16:** Uses one or two 16-bit code units to represent a Unicode code point.
  - **UTF-32:** Uses a fixed 32-bit code unit for each Unicode code point.

## Practical Experience

During this lab, I explored how text is represented and encoded by computers.

I learned how ASCII maps characters to numerical values, why ASCII has limitations, how encoding mismatches can produce gibberish characters, and why Unicode and UTF encoding formats are important for supporting different languages and symbols.

## SOC Analyst Relevance

Understanding data encoding is useful for a SOC Analyst because security investigations often involve examining text, files, logs, and data exchanged between systems.

This knowledge provides a foundation for:
- Understanding how text is stored and transmitted as bytes.
- Recognizing encoding mismatches that may cause unreadable log entries.
- Understanding ASCII and hexadecimal values in technical outputs.
- Learning how different encoding formats affect text interpretation.
- Supporting further study of log analysis, digital forensics, and network data inspection.

As I continue preparing for a SOC Analyst Level 1 role, I will build on these fundamentals while learning how to inspect files, interpret technical data, and investigate suspicious activity.

## Key Takeaways

- Computers represent text using numerical values that can be encoded into bytes.
- ASCII uses 7 bits and supports 128 standard character values.
- Standard ASCII cannot represent every character used by languages around the world.
- An encoding mismatch can cause text to appear as gibberish.
- Unicode provides code points for characters across many writing systems.
- UTF-8, UTF-16, and UTF-32 encode Unicode code points in different ways.
- Understanding encoding helps when interpreting files, logs, and other technical data.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Pre Security
- **Room:** Data Encoding
- **Topics:** Text representation, ASCII, Unicode, and UTF encodings
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.
