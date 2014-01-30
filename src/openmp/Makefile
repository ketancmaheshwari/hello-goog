ifeq ($(SYSTEM), linux)
    CC=icc
    CFLAGS=-openmp
endif

EXECS=hello.o

all: $(EXECS)

hello.o: hello.c
	$(CC) $(CFLAGS) -o $@ $?

clean:
	rm -f *.o $(EXECS)
