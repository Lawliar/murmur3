#include "DRIFT_HASH.h"

int
main(){
    uint32_t addr = 0x08001904;
    uint32_t ret = DRIFT_HASH_LOOKUP(addr);
    printf("%d\n",ret);
}
