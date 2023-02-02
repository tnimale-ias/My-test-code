function has_dot(str)
  if string.find(str, "com", 1, true) ~= nil then
        return false
  else
        return string.find(str, ".", 1, true) ~= nil
  end
end


function delete_dir(path)

local cmd = "ls -1 " .. path
local handle = io.popen(cmd)
local filelist = handle:read("*all")
handle:close()

local files = {}
for filename in string.gmatch(filelist, "%S+") do
  table.insert(files, filename)
end

for filename in string.gmatch(filelist, "%S+") do
if has_dot(filename) then
        os.remove(path .. filename)
else
        delete_dir(path .. filename .. "/")
        print(path .. filename .. "/")
end
end

end


delete_dir("/test/")

