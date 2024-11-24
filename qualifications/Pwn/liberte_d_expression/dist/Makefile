CC = gcc
CFLAGS = -fno-stack-protector -no-pie
TARGET = liberte
SRC = liberte.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGET)

.PHONY: all clean
