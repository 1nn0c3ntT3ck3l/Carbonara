#ifndef WALLET_UTILS_H
#define WALLET_UTILS_H

void start_rpc_server(int port);
void simulate_payload_injection(const char *payload);
void fake_transfer(const char *wallet, double amount) {
    printf("[*] Simulated transfer of %.4f ETH from %s\n", amount, wallet);
}
#endif
