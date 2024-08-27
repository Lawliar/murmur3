CFLAGS = -O3 -Wall
target = DRIFT-Template
common_dir = ../../firmware/Common/hash
target_dir = ../../firmware/$(target)/CommonDRIFT
inc_dirs = -I. -I$(common_dir) -I$(target_dir)
.PHONY: all clean tests

dbg_flags = -O0 -g
all: example
example: DRIFT_HASH.o murmur3.o DRIFT_HASH_CONF.o
	gcc $(dbg_flags) $(inc_dirs) $^ main.c -o $@

DRIFT_HASH.o: $(common_dir)/DRIFT_HASH.c
	gcc $(dbg_flags) $(inc_dirs) $< -c -o $@

DRIFT_HASH_CONF.o: $(target_dir)/DRIFT_HASH_CONF.c
	gcc $(dbg_flags) $(inc_dirs) $< -c -o $@


tests: test.o murmur3.o
	$(CC) $^ -o $@
	./tests

shared: murmur3.c murmur3.h
	$(CC) -fPIC -O3 -c murmur3.c
	$(CC) -shared -Wl,--export-dynamic murmur3.o -o libmurmur3.so

clean:
	rm -rf example *.o *.so
