import time as tm
from functools import wraps

timings = []


def tic():

	timings.append(tm.clock())


def toc(message=True,precision=3):

	try:

		elapsed = tm.clock() - timings.pop()

		if message:
			print('{:5.{precision}f} seconds elapsed.'.format(elapsed,precision=precision))

		return elapsed

	except IndexError as e:

		print('Oops! Make sure to start timing by calling tic() before calling toc().')


def tictoc(message=True,return_elapsed=False,precision=3):

	def decorator(func):

		@wraps(func)
		def wrapped(*args,**kwargs):

			start = tm.clock()
			retValue = func(*args,**kwargs)
			elapsed = tm.clock() - start

			if message:
				print('{:5.{precision}f} seconds elapsed.'.format(elapsed,precision=precision))

			if return_elapsed:
				return retValue, elapsed

			else:
				return retValue

		return wrapped

	return decorator


def main():
	"""Run this for testing."""

	print('Running tests for timing.py -- this should take about 8 seconds.')

	def slow(n=3):

		print('\n...intermission...\n')

		tm.sleep(n)

		print('Hello World ({}sec slept)'.format(n))

	tic()
	slow(3)
	toc()

	@tictoc(precision=5)
	def decorated_slow(n=3):

		print('\n...intermission...\n')

		tm.sleep(n)

		print('(Decorated function example)')
		print('Hello World ({}sec slept)'.format(n))

	decorated_slow()
	decorated_slow(2)


if __name__ == '__main__':
	main()