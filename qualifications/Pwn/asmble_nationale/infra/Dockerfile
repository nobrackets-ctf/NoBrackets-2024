FROM debian:bookworm-slim

# Update apt
RUN apt update

# Install socat
RUN apt install -y socat

# Remove apt lists to reduce image size
RUN rm -rf /var/lib/apt/lists/*

# Copy asmble_nationale to /app
COPY asmble_nationale /app/

# Copy flag to /flag.txt
COPY flag.txt /

# Add a user named "chall"
RUN useradd chall

# Make /app/asmble_nationale executable by chall
RUN chmod +x /app/asmble_nationale && chown chall:chall /app/asmble_nationale

# Disable access to /tmp and /var/tmp for chall user
RUN chmod 700 /tmp /var/tmp && \
    chown root:root /tmp /var/tmp


# Switch to chall user
USER chall

# Launch socat on port 10201
CMD ["socat", "TCP-LISTEN:10201,reuseaddr,fork", "EXEC:/app/asmble_nationale,pty,stderr"]
