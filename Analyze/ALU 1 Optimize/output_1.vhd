library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity alu is
Port ( inp_a : in signed(3 downto 0);
inp_b : in signed(3 downto 0);
sel : in STD_LOGIC_VECTOR(2 downto 0);
out_alu : out signed(3 downto 0));
end alu;

architecture Behavioral of alu is

signal tmp_add, tmp_sub : signed(3 downto 0);
begin
-- Precompute common operations
tmp_add <= inp_a + inp_b;
tmp_sub <= inp_a - inp_b;

process(inp_a, inp_b, sel, tmp_add, tmp_sub)
begin
case sel is
when "000" => -- addition
out_alu <= tmp_add;
when "001" => -- subtraction
out_alu <= tmp_sub;
when "010" => -- subtract 1
out_alu <= inp_a - 1;
when "011" => -- add 1
out_alu <= inp_a + 1;
when "100" => -- AND
out_alu <= inp_a and inp_b;
when "101" => -- OR
out_alu <= inp_a or inp_b;
when "110" => -- NOT
out_alu <= not inp_a;
when "111" => -- XOR
out_alu <= inp_a xor inp_b;
when others =>
out_alu <= (others => '0'); -- Default case to avoid latches

end case;

end process;

end Behavioral;
