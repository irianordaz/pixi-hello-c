# Variables for the compiler and flags
CC = gcc
CFLAGS = -Wall -g
TARGET = hello

# Default rule: build the executable
all: $(TARGET)

$(TARGET): hello.c
	$(CC) $(CFLAGS) -o $(TARGET) hello.c

# Clean rule to remove the binary
clean:
	rm -f $(TARGET)

