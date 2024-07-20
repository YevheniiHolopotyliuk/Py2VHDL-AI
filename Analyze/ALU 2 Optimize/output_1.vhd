library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu is
    generic (
        W : integer := 16  -- Data width
    );
    port (
        sel : in  std_logic_vector(2 downto 0);  -- Operation selector
        a   : in  std_logic_vector(W-1 downto 0); -- First operand
        b   : in  std_logic_vector(W-1 downto 0); -- Second operand
        cf  : out std_logic; -- Carry flag
        zf  : out std_logic; -- Zero flag
        ov  : out std_logic; -- Overflow flag
        sf  : out std_logic; -- Sign flag
        y   : out std_logic_vector(W-1 downto 0) -- Result
    );
end entity alu;

architecture RTL of alu is
    signal a_us, b_us   : unsigned(W-1 downto 0); -- Arith. unit 1st & 2nd operand
    signal arith_out    : unsigned(W downto 0); -- Arith. unit result
    signal logic_out    : std_logic_vector(W-1 downto 0); -- Logic unit result
    signal y_i          : std_logic_vector(W-1 downto 0); -- Global result
begin

    -- Sign extension
    a_us <= unsigned(a);
    b_us <= unsigned(b);

    -- global output assignment
    y <= y_i;

    -- ALU logic
    arith_op: process(sel, a_us, b_us) is
    begin
        case sel is
            when "000" =>
                arith_out <= (others => '0');
                y_i <= (others => '0');
            when "001" =>
                arith_out <= ('0' & a_us);
                y_i <= a;
            when "010" =>
                arith_out <= ('0' & a_us) + b_us;
                y_i <= std_logic_vector(a_us + b_us);
            when "011" =>
                arith_out <= ('0' & a_us) - b_us;
                y_i <= std_logic_vector(a_us - b_us);
            when "100" =>
                logic_out <= not a;
                y_i <= not a;
            when "101" =>
                logic_out <= a and b;
                y_i <= a and b;
            when "110" =>
                logic_out <= a or b;
                y_i <= a or b;
            when "111" =>
                logic_out <= a xor b;
                y_i <= a xor b;
            when others =>
                null;
        end case;
    end process arith_op;

    -- Output flags
    cf <= arith_out(W);
    sf <= y_i(W-1);
    -- was errors in Vivado
    -- zf <= '1' when y_i = (others => '0') else '0';
    -- from original code was insert the line for replace 72 line
    zf <= '1' when y_i = (y_i'range => '0') else
		  '0';

    ov <= '1' when (sel = "010" and ((a_us(W-1) = '0' and b_us(W-1) = '0' and arith_out(W-1) = '1') or
                                    (a_us(W-1) = '1' and b_us(W-1) = '1' and arith_out(W-1) = '0'))) or
                   (sel = "011" and ((a_us(W-1) = '0' and b_us(W-1) = '1' and arith_out(W-1) = '1') or
                                    (a_us(W-1) = '1' and b_us(W-1) = '0' and arith_out(W-1) = '0')))
         else '0';

end architecture RTL;