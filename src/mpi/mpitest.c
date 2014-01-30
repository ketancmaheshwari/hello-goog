#include <stdio.h>
#include <unistd.h>
#include <mpi.h>
#include <fcntl.h>

int main (int argc, char *argv[])
{
  int rank;
  char *ifile = argv[1];
  char *ofile = argv[2];
  int sleeptime = atoi(argv[3]);
  char hostname[1024];

  MPI_Init (&argc, &argv);		
  MPI_Comm_rank (MPI_COMM_WORLD, &rank);
  gethostname(hostname, sizeof hostname);

  if (rank==0) {
     printf("Hostname=%s, rank=%d, ifile=%s ofile=%s sleeptime=%d\n", hostname, rank, ifile, ofile, sleeptime);
     int ifd = open(ifile,O_RDONLY);
     int ofd = open(ofile,O_WRONLY|O_CREAT,0664);
     char buf[1024*1024];
     for(;;) {
        int rc = read(ifd, buf, sizeof(buf));
        if (rc <= 0) {
           close(ifd);
           close(ofd);
           break;
        }
        write(ofd, buf, rc);
     }
  } 

  else printf("Hostname=%s, rank=%d\n", hostname, rank);

  sleep(sleeptime); 
  MPI_Finalize();
}
