-- ./out < input4.txt

import qualified Data.Text as T
import Data.List
import Data.Char
import Debug.Trace
import Text.Regex
import Data.Maybe

-- Name, Encrypted characters, Id, Checksum
data Room = Room String String Int String deriving (Show)

parse :: String -> [Room]
parse s = map parseRoom $ lines s

wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

join :: [String] -> String
join [] = []
join (x:xs) = x ++ join xs

shift :: Int -> Char -> Char
shift _ '-' = ' '
shift n c = chr $ (mod ((ord c - 97) + n) 26) + 97

decrypt :: String -> Int -> String
decrypt s key = map (shift key) s

parseRoom2 :: String -> Room
parseRoom2 s = Room (decrypt name idNum) cryptoName idNum csum
  where pattern = mkRegex "([a-z-]*)-([0-9]*)\\[([a-z]*)\\]"
        (name:i:csum:_) = fromJust $ matchRegex pattern s
        cryptoName = sort $ filter (not . (`elem` "-")) $ name
        idNum = read i

parseRoom :: String -> Room
parseRoom s = Room name (sort $ join cryptoName) idNum (init $ last idCheck)
  where parts = wordsWhen (=='-') s
        cryptoName = init parts
        idCheck = wordsWhen (=='[') $ last parts
        idNum = (read (head idCheck) :: Int)
        name = decrypt (intercalate "-" cryptoName) idNum

count :: String -> [(Char, Int)]
count [] = []
count (x:xs) = count' (x, 1) xs

count' :: (Char, Int) -> String -> [(Char, Int)]
count' acc [] = [acc]
count' (c, n) (x:xs)
  | c == x    = count' (c, n+1) xs
  | otherwise = (c, n) : (count' (x, 1) xs)

charOrder :: Char -> Char -> Ordering
charOrder c1 c2
  | c1 > c2 = GT
  | c1 == c2 = EQ
  | c1 < c2 = LT

order :: (Char, Int) -> (Char, Int) -> Ordering
order (c1, n1) (c2, n2)
  | n1 < n2  = GT
  | n1 == n2 = charOrder c1 c2
  | n1 > n2  = LT

checksum :: String -> String
checksum s = take 5 $ map fst $ sortBy order $ count s

valid :: Room -> Bool
valid (Room name crypto i csum) = csum == checksum crypto

task1 :: [Room] -> Int
task1 input = sum [ getId x | x <- input, valid x]
  where getId (Room _ _ i _) = i

task2 input = head [ i | (Room (n:name) crypto i csum) <- input, n == 'n' ]

--main = print $ valid $ parseRoom "totally-real-room-200[decoy]"

--main = print $ parseRoom2 "aaaaa-bbb-z-y-x-123[abxyz]"
main = interact $ show . task2 . parse
