# Comprehensive Guide to Python Errors and Exceptions (Python 3.14.6)

## 1. Introduction to Python Error Categories

Python categorizes errors into two primary types: syntax errors and exceptions. Understanding when these errors are detected and how they behave is fundamental to writing robust code.

| Feature | Syntax Errors | Exceptions |
| :--- | :--- | :--- |
| **Common Name** | Parsing Errors | Execution Errors |
| **Detection Timing** | During the parsing phase (before the code runs) | During program execution |
| **Nature** | Violations of Python's grammar and structural rules | Errors occurring during valid syntax (e.g., logic or environment issues) |
| **Fatal Context** | Unconditionally fatal; prevents execution | Not necessarily fatal; can be intercepted and handled |

---

## 2. Syntax Errors (Parsing Errors)

Syntax errors occur when the Python parser cannot understand the structure of the code.

*   **Visual Feedback:** The parser repeats the offending line and uses small arrows to point at the exact position where the error was detected.
*   **Detection vs. Fix Location:** It is critical to note that the indicated position is where the error was detected, which is not always where the fix is required. For example, a missing colon at the end of an `if` statement might only be flagged by the parser when it reaches the indented code on the next line.
*   **Metadata:** Python provides the file name and the line number where the parser encountered the error to assist in debugging.

---

## 3. Exceptions (Execution Errors)

Exceptions are errors detected during the execution of a statement or expression, even if the syntax is correct. If an exception is not handled, Python generates a detailed error message.

### Components of an Exception Message
*   **Stack Traceback:** This shows the context of the error, listing the sequence of source lines that led to the exception. Note that lines read from standard input (interactive mode) are not displayed in the traceback.
*   **Exception Type:** The name of the built-in exception (e.g., `ZeroDivisionError`, `NameError`, `TypeError`). These names are built-in identifiers, not reserved keywords.
*   **Exception Detail:** The final part of the message provides specific information about why the exception was raised.

---

## 4. Handling Exceptions with the try...except Statement

The `try...except` statement is the primary mechanism for managing errors during runtime.

### The Mechanical Workflow
1. The `try` clause (the code block between `try` and `except`) is executed.
2. If no exception occurs, the `except` clause is skipped.
3. If an exception occurs, the rest of the `try` clause is immediately skipped.
4. If the exception type matches the name in the `except` clause, the `except` clause is executed. Execution then continues after the entire `try`/`except` block.
5. If an unhandled exception occurs (no matching clause is found), it is passed to outer `try` statements. If still unhandled, the program terminates with an error.

### Handling Multiple Exceptions
*   **Tuples:** You can catch multiple specific exceptions in a single clause using a parenthesized tuple: `except (RuntimeError, TypeError, NameError):`.
*   **Class Hierarchy:** A handler matches an exception if it lists the exception's class or a base class thereof. Crucially, this is one-way: a base class handler (like `Exception`) will catch derived class errors, but a derived class handler will not catch a base class error.
*   **Priority:** Only the first matching `except` clause is triggered.

### Arguments and Hierarchy
*   **The as Keyword:** Use `except Exception as inst:` to bind the exception instance to a variable. While the arguments are stored in the `.args` attribute, built-in exception types define `__str__()` to print all arguments directly without needing to access `.args` explicitly.
*   **BaseException vs. Exception:** `BaseException` is the root of all exceptions. `Exception` is the base for all non-fatal errors.
*   **Handling Best Practices:** Avoid catching `BaseException`. It includes `SystemExit` and `KeyboardInterrupt`, which are used to terminate programs. Catching these by accident can prevent a user from stopping a script with Control-C.
*   **The Log and Re-raise Pattern:** A common professional pattern involves catching a general `Exception`, logging or printing the error, and then using a bare `raise` to re-raise it. This allows the current block to record the error while still allowing the caller to handle the exception.

---

## 5. The else Clause in Exception Handling

An optional `else` clause can follow all `except` clauses. It executes only if the `try` clause did not raise an exception.

> **Architectural Insight:** Using the `else` clause is superior to bloating the `try` block. It narrows the scope of the "protected" code, ensuring that you don't accidentally catch an exception raised by code that was not the intended target of your error handling.

---

## 6. Raising and Re-raising Exceptions

The `raise` statement allows you to force a specific exception.

*   **Syntax:** The argument must be an exception instance or class (which derives from `BaseException`). If a class is used, Python implicitly instantiates it by calling the constructor with no arguments.
*   **Re-raising:** If you need to detect that an error occurred but do not want to stop its propagation, use a bare `raise` statement inside the handler to pass the original exception up the call stack.

---

## 7. Exception Chaining

Chaining provides a history of how errors occurred.

*   **Implicit Chaining:** If an exception is raised inside an `except` block while another is already being handled, the original is attached to the new one for debugging context.
*   **Explicit Chaining:** Use `raise NewError from OldError` to clarify that one exception is a direct result of another (exception transformation).
*   **Disabling Chaining:** If you want to suppress the history, use the `from None` idiom: `raise MyError from None`.

---

## 8. Defining Clean-up Actions (finally Clause)

The `finally` clause defines actions that must execute under all circumstances, typically used for releasing external resources like files or network connections.

### Complex finally Behaviors
*   **Execution Timing:** `finally` runs as the very last task of the `try` statement, regardless of whether an exception was raised, handled, or ignored.
*   **Unhandled Exceptions:** If an exception is not handled by an `except` clause (or occurs inside an `except` or `else` block), it is temporarily stored and re-raised after the `finally` block completes.
*   **Control Flow Interruption:** If a `finally` block executes a `break`, `continue`, or `return`, any pending exception is discarded.
*   **Return Value Overriding:** If the `finally` block contains a `return` statement, that value will override any return value from the `try` clause.

> ⚠️ **Python 3.14 (PEP 765) Warning:** Because the behaviors above can lead to silent errors, Python 3.14 now emits a `SyntaxWarning` if `break`, `continue`, or `return` are used inside a `finally` block.

---

## 9. Predefined Clean-up Actions (The with Statement)

The `with` statement is the Pythonic way to handle resource management. While a standard file `open` might leave a file descriptor hanging if an error occurs, the `with` statement ensures the resource is closed promptly and correctly the moment the block is exited, even if an exception was raised during processing.

---

## 10. User-defined Exceptions

Professional Python developers often define custom exceptions to provide clear, domain-specific error reporting.

*   **Requirements:** Custom exceptions must derive from the `Exception` class.
*   **Naming:** By convention, custom exception names should end in "Error".
*   **Industry Context:** Many standard library modules follow this pattern (e.g., `os.error`). Custom exceptions should stay simple, focusing on providing attributes that help handlers extract specific diagnostic data.

---

## 11. Raising and Handling Multiple Unrelated Exceptions

In scenarios like concurrent programming, multiple tasks might fail simultaneously.

*   **ExceptionGroup:** This wraps a list of exception instances so they can be raised as a single unit.
*   **The except\* Syntax:** This allows you to selectively handle specific exception types within an `ExceptionGroup`. Each `except*` clause "picks out" its matching types from the group while letting the rest continue to propagate.
*   **Constraint:** Nested exceptions in an `ExceptionGroup` must be instances, not types.

---

## 12. Enriching Exceptions with Notes

Python 3.11+ introduced the `add_note(note)` method, allowing developers to append string-based context to an exception after it has been caught but before it is re-raised.

### The Bridge to ExceptionGroups
Notes are particularly critical when using `ExceptionGroup`. Because a group may contain many unrelated errors, the generic exception type is often insufficient. By using `add_note()`, you can enrich each individual error with specific context (like which task failed or the timestamp of the failure) before bundling them into the group. These notes are rendered in the standard traceback in the order they were added.