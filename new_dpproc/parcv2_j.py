#=========================================================================
# parcv2 j tests
#=========================================================================

from new_pymtl import *

from new_pmlib.SparseMemoryImage import SparseMemoryImage

#---------------------------------------------------------------------------
# String based Assembly Tests
#---------------------------------------------------------------------------
# Directed string based assembly tests

# test_start string

test_start = """
  .text;
  .align  4;
  .global _test;
  .ent    _test;
  _test:
"""

# test_end string

test_end   = """
  .end    _test;
"""

def j_asm():

  asm_str = \
    ( test_start +
       """
       j     1f
       mtc0  $4, $1
       nop
       nop
       nop
       nop
    1: li    $3, 1
       mtc0  $3, $1
       nop; nop; nop; nop;
       nop; nop; nop; nop;
       """
     + test_end )

  mem_delay       = 0
  sparse_mem_img  = SparseMemoryImage( asm_str = asm_str )
  expected_result = 1

  return [ mem_delay, sparse_mem_img, expected_result ]

#---------------------------------------------------------------------------
# VMH File Assembly Tests
#---------------------------------------------------------------------------
# Self-checking VMH file based assembly tests

# VMH Files location

vmh_dir = '../tests/build/vmh/'

# test with no delay

def j_vmh_delay0():

  test_file = vmh_dir + 'parcv2-j.vmh'

  mem_delay       = 0
  sparse_mem_img  = SparseMemoryImage( vmh_filename = test_file )
  expected_result = 1

  return [ mem_delay, sparse_mem_img, expected_result ]

# test with delay

def j_vmh_delay5():

  test_file = vmh_dir + 'parcv2-j.vmh'

  mem_delay       = 5
  sparse_mem_img  = SparseMemoryImage( vmh_filename = test_file )
  expected_result = 1

  return [ mem_delay, sparse_mem_img, expected_result ]