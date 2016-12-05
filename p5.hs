import Data.Hash.MD5
import Data.String.Utils
import Data.Char
import Debug.Trace

input_test = "abc"
input = "abbhdwsy"

-- Slow!!
slowMD5s key = filter (startswith "00000") $ map (md5s . Str . ((++) key) . show) [0..]

get n = last . (take n)

intVal :: Char -> Int
intVal c = (ord c) - 48

idVal :: String -> (Int, Char)
idVal ('0':'0':'0':'0':'0':i:e:_) = (intVal i, e)
idVal _ = (-1, '#')

idVals :: [String] -> [(Int, Char)]
idVals ls = [ (i, c) | (i, c) <- map idVal ls, i >= 0, i < 8 ]

notIn :: [(Int, Char)] -> (Int, Char) -> Bool
notIn [] _ = True
notIn ((i1,_):ls) (i2,c) = i1 /= i2 && notIn ls (i2,c)

onlyFirstId :: [(Int, Char)] -> [(Int, Char)] -> [(Int, Char)]
onlyFirstId _ [] = []
onlyFirstId acc (t:ts) = case notIn acc t of
  True  -> ((traceShowId t):onlyFirstId (t:acc) ts)
  False -> onlyFirstId acc ts

task1 = take 3 $ map (get 6) $ slowMD5s input_test

task2 = take 8 $ onlyFirstId [] $ idVals $ slowMD5s input

main = print $ task2

