function calculate_cont_frm(filename, num, den)
  f_temp = mopen(filename, 'wt');
  H = cont_frm(num, den);
  [A, B, C, D] = abcd(H);
  cont_frm_write(A, B, C, D, f_temp);
  mclose(f_temp);
endfunction


function cont_frm_write(varargin)
  loop = argn(2);
  f_temp = varargin(loop);
  mfprintf(f_temp, '[')
  for k = 1:(loop-1)
    variable = varargin(k)
    [m, n] = size(variable)
    for y = 1:n
      for z = 1:m
        if (k == loop-1) & (y == n) & (z == m) then
          mfprintf(f_temp, '%.17g', variable(z, y))
        else
          mfprintf(f_temp, '%.17g,', variable(z, y))
        end
      end
    end
  end
  mfprintf(f_temp, ']')
endfunction
