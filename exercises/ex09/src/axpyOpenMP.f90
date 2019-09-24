subroutine axpy(n, a, X, Y, Z)
use iso_fortran_env, only: real64
implicit none
integer :: n
real(real64) :: a
real(real64) :: X(*), Y(*), Z(*)
integer :: i

!$omp parallel default(none), shared(n, a, X, Y, Z), private(i)
!$omp do
  do i = 1, n
    Z(i) = a * X(i) + Y(i)
  end do
!$omp end do
!$omp end parallel

end subroutine axpy

program axpyProg
use iso_fortran_env, only: real64
!use omp_lib
implicit none
real(real64) :: a
real(real64), allocatable :: X(:), Y(:), Z(:)
integer :: n

  n = 2**10

  allocate(X(n))
  allocate(Y(n))
  allocate(Z(n))

  call random_seed
  call random_number(a)
  call random_number(X)
  call random_number(Y)

  call axpy(n, a, X, Y, Z)

  print *, maxval(abs(Z)), maxval(abs(Z / (a * X + Y) - 1.0_real64))

  deallocate(X)
  deallocate(Y)
  deallocate(Z)

end program axpyProg
