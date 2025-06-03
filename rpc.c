#include <stdio.h>
#include <unistd.h>

void start_rpc_server(int port) {
    printf("[*] JSON-RPC server listening on port %d\n", port);
    sleep(2);
    printf("[+] Received handshake from wallet.\n");
}
