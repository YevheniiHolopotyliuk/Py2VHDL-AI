library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity alu is
generic (
W : integer := 16 -- Data width
);
port (
sel : in std_logic_vector(2 downto 0); -- Operation selector
a : in std_logic_vector(W-1 downto 0); -- First operand
b : in std_logic_vector(W-1 downto 0); -- Second operand
cf : out std_logic; -- Carry flag
zf : out std_logic; -- Zero flag
ov : out std_logic; -- Overflow flag
sf : out std_logic; -- Sign flag
y : out std_logic_vector(W-1 downto 0) -- Result
);
end entity alu;
architecture RTL of alu is
signal a_us, b_us, result_us : unsigned(W downto 0); -- Extended to W+1 for carry
signal res : std_logic_vector(W-1 downto 0);
begin
-- Convert inputs to unsigned
a_us <= unsigned('0' & a);
b_us <= unsigned('0' & b);
-- Main process handling both arithmetic and logic operations
process(sel, a_us, b_us)
begin
case sel is
when "000" => -- Logic NOT operation
res <= not a;
result_us <= (others => '0');
when "001" => -- Logic AND operation
res <= a and b;
result_us <= (others => '0');
when "010" => -- Logic OR operation
res <= a or b;
result_us <= (others => '0');
when "011" => -- Logic XOR operation
res <= a xor b;
result_us <= (others => '0');
when "100" => -- Arithmetic pass-through a
result_us <= a_us;
when "101" => -- Arithmetic addition a + b
result_us <= a_us + b_us;
when "110" => -- Arithmetic subtraction a - b
result_us <= a_us - b_us;
when others => -- Default case for reset, do nothing
res <= (others => '0');
result_us <= (others => '0');
end case;
end process;
-- Output assignment
y <= res when (sel(2) = '0') else std_logic_vector(result_us(W-1 downto 0));
-- Flags
cf <= result_us(W); -- Carry flag from extended result
zf <= '1' when y = (others => '0') else '0'; -- Zero flag
sf <= y(W-1); -- Sign flag
ov <= '1' when (
(sel = "101" and ((a_us(W-1) = '0' and b_us(W-1) = '0' and result_us(W-1) = '1') or
(a_us(W-1) = '1' and b_us(W-1) = '1' and result_us(W-1) = '0'))) or
(sel = "110" and ((a_us(W-1) = '1' and b_us(W-1) = '0' and result_us(W-1) = '0') or
(a_us(W-1) = '0' and b_us(W-1) = '1' and result_us(W-1) = '1'))))
else '0'; -- Overflow flag
end architecture RTL;
