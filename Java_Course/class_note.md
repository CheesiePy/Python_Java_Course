# Java Course Lesson 2 - Class Note

## 1. Java Data Types

### 1.1 Primitive Data Types

#### 1.1.1 Integer Types

| Type | Size | Range |
| :--- | :--- | :--- |
| byte | 1 byte | -128 to 127 |
| short | 2 bytes | -32,768 to 32,767 |
| int | 4 bytes | -2,147,483,648 to 2,147,483,647 |
| long | 8 bytes | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |

#### 1.1.2 Floating Point Types

| Type | Size | Range |
| :--- | :--- | :--- |
| float | 4 bytes | 1.4E-45 to 3.4028235E38 |
| double | 8 bytes | 4.9E-324 to 1.7976931348623157E308 |

#### 1.1.3 Character Type

| Type | Size | Range |
| :--- | :--- | :--- |
| char | 2 bytes | 0 to 65,535 |

#### 1.1.4 Boolean Type

| Type | Size | Range |
| :--- | :--- | :--- |
| boolean | 1 bit | true or false |

### 1.2 Non-Primitive Data Types

#### 1.2.1 String

String is a sequence of characters. String is a non-primitive data type. String is a class in Java. String is immutable. String is a sequenc of characters. String is a non-primitive data type. String is a class in Java. String is immutable.


```java
String str = "Hello World";
```


#### 1.2.2 Array

Array is a collection of similar data types. Array is a non-primitive data type. Array is a class in Java. Array is mutable. Array is a collection of similar data types. Array is a non-primitive data type. Array is a class in Java. Array is mutable.

```java
int[] arr = {1, 2, 3, 4, 5};
```

## 2. Java Operators

### 2.1 Arithmetic Operators

| Operator | Description | Example |
| :--- | :--- | :--- |
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| % | Modulus | a % b |
| ++ | Increment | ++a |
| -- | Decrement | --a |

### 2.2 Assignment Operators

| Operator | Description | Example |
| :--- | :--- | :--- |
| = | Simple assignment | c = a + b |
| += | Add and assignment | c += a |
| -= | Subtract and assignment | c -= a |
| *= | Multiply and assignment | c *= a |

### 2.3 Comparison Operators

| Operator | Description | Example |
| :--- | :--- | :--- |
| == | Equal to | a == b |
| != | Not equal to | a != b |
| > | Greater than | a > b |
| < | Less than | a < b |
| >= | Greater than or equal to | a >= b |
| <= | Less than or equal to | a <= b |

### 2.4 Logical Operators

| Operator | Description | Example |
| :--- | :--- | :--- |
| && | Logical and | a && b |
| \|\| | Logical or | a \|\| b |
| ! | Logical not | !a |

### 2.5 Bitwise Operators

| Operator | Description | Example |
| :--- | :--- | :--- |
| & | Bitwise and | a & b |
| \| | Bitwise or | a \| b |
| ^ | Bitwise xor | a ^ b |
| ~ | Bitwise not | ~a |
| << | Left shift | a << 1 |
| >> | Right shift | a >> 1 |
| >>> | Zero fill right shift | a >>> 1 |

## 3. Java Control Statements

### 3.1 if-else Statement

```java
if (condition) {
    // do something
} else {
    // do something
}
```

### 3.2 switch Statement

```java
switch (expression) {
    case value1:
        // do something
        break;
    case value2:
        // do something
        break;
    default:
        // do something
}
```

### 3.3 for Statement

```java
for (initialization; condition; increment) {
    // do something
}
```

### 3.4 while Statement

```java
while (condition) {
    // do something
}
```

### 3.5 do-while Statement

```java
do {
    // do something
} while (condition);
```

### 3.6 break Statement

```java
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;
    }
    System.out.println(i);
}
```


### 3.7 continue Statement

```java
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        continue;
    }
    System.out.println(i);
}
```

## 4. Java Methods

### 4.1 Method Declaration

```java
public static void main(String[] args) {
    // do something
}
```

### 4.2 Method Parameters

```java
public void myMethod(String name, int age) {
    // do something
}

```


### 4.3 Method Overloading

```java
public void myMethod(String name) {
    // do something
}

public void myMethod(String name, int age) {
    // do something
}


```

### 4.4 Method Return

```java
public int myMethod(int a, int b) {
    return a + b;
}
```

## 5. Java Arrays

### 5.1 Array Declaration

```java
int[] arr = new int[5];
```

### 5.2 Array Initialization

```java
int[] arr = {1, 2, 3, 4, 5};
```

### 5.3 Array Access

```java
int[] arr = {1, 2, 3, 4, 5};
System.out.println(arr[0]);
```

### 5.4 Array Length

```java
int[] arr = {1, 2, 3, 4, 5};
System.out.println(arr.length);
```






