subroutine axpy(n, a, X, Y, Z)
use iso_fortran_env, only: real64
implicit none
integer :: n
real(real64) :: a
real(real64) :: X(*), Y(*), Z(*)
integer :: i

  do i = 1, n
    Z(i) = a * X(i) + Y(i)
  end do

end subroutine axpy

program axpyProg
use iso_fortran_env, only: real64
!use mpi

implicit none
include 'mpif.h'
real(real64) :: a_P
real(real64), allocatable :: X(:), Y(:), Z(:)
real(real64), allocatable :: X_P(:), Y_P(:), Z_P(:)
integer :: n, n_P
integer :: nProcs, procN, err

  n = 2**10

  call mpi_init(err)

  call mpi_comm_size(mpi_comm_world, nProcs, err)
  call mpi_comm_rank(mpi_comm_world, procN, err)

  if (procN == 0) then
    allocate(X(n))
    allocate(Y(n))
    allocate(Z(n))

    call random_seed
    call random_number(a_P)
    call random_number(X)
    call random_number(Y)
  end if

  n_P = n / nProcs

  allocate(X_P(n_P))
  allocate(Y_P(n_P))
  allocate(Z_P(n_P))

  call mpi_bcast(a_P, 1, mpi_double_precision, 0, mpi_comm_world, err)
  call mpi_scatter(X, n_P, mpi_double_precision, X_P, n_P, mpi_double_precision, 0, mpi_comm_world, err)
  call mpi_scatter(Y, n_P, mpi_double_precision, Y_P, n_P, mpi_double_precision, 0, mpi_comm_world, err)

  call axpy(n_P, a_P, X_P, Y_P, Z_P)

  deallocate(X_P)
  deallocate(Y_P)

  call mpi_gather(Z_P, n_P, mpi_double_precision, Z, n_P, mpi_double_precision, 0, mpi_comm_world, err)

  deallocate(Z_P)

  if (procN == 0) then
    print *, maxval(abs(Z)), maxval(abs(Z / (a_P * X + Y) - 1.0_real64))

    deallocate(X)
    deallocate(Y)
    deallocate(Z)
  end if

  call mpi_finalize(err)

end program axpyProg
