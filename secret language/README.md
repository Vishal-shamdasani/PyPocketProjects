# Encode and Decode Message Project

This project is a simple Python program that allows users to encode or decode a message using a basic string manipulation technique. The program prompts the user to select an action (encode or decode) and then processes the input message accordingly.

---

## Features
- **Encoding**: Rearranges the input message by moving the first character to the end and reversing the string.
- **Decoding**: Reverses the string and adjusts the character positions to retrieve the original message.
- Includes basic validation to ensure the message length is at least three characters.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Vishal-shamdasani/PyPocketProjects/tree/main/secret%20language.git
   ```
2. Navigate to the project directory:
   ```bash
   cd secret\ language
   ```
3. Run the Python script:
   ```bash
   python encode_decode.py
   ```
4. Follow the prompts:
   - Enter `C` to encode a message.
   - Enter `D` to decode a message.

---

## Code Explanation
### Encoding
1. Input a message.
2. Validate that the message has at least three characters.
3. Move the first character to the end of the string.
4. Reverse the modified string.
5. Display the encoded message.

### Decoding
1. Input an encoded message.
2. Validate that the message has at least three characters.
3. Reverse the string.
4. Adjust the character positions to retrieve the original message.
5. Display the decoded message.

---

## Example Usage
### Encoding
```
if you want to code a message type C
else if you want to decode type D
C
enter your message it should be more than 3 letters long: hello
olleh
```

### Decoding
```
if you want to code a message type C
else if you want to decode type D
D
enter the message you want to decode: olleh
hello
```

---

## Error Handling
- If the input message has fewer than three characters, a `ValueError` is raised with the message: *"The message should be at least 3 letters long"*.
- If an invalid option is selected, a `TypeError` is raised with the message: *"Given argument is not an option"*.

---

## Improvements
This program can be further enhanced by:
- Adding support for different encoding/decoding algorithms.
- Allowing the user to save encoded or decoded messages to a file.
- Building a GUI for a better user experience.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance this project.

---

## Repository Link
[Encode and Decode Message Project on GitHub](https://github.com/Vishal-shamdasani/PyPocketProjects/tree/main/secret%20language)

