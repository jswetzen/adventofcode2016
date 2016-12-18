-- ./out < input3.txt

parse :: String -> [[Int]]
parse = (map $ (\l -> map (\x -> read x :: Int) (words l))) . lines

possible :: [Int] -> Bool
possible (a:b:c:[]) = and [a+b>c, a+c>b, b+c>a]

transform :: [[Int]] -> [[Int]]
transform [] = []
transform (l1:l2:l3:ls) = (transform3 l1 l2 l3) ++ (transform ls)

transform3 :: [Int] -> [Int] -> [Int] -> [[Int]]
transform3 [] [] [] = []
transform3 (a:as) (b:bs) (c:cs) = [[a, b, c]] ++ transform3 as bs cs

task1 input = length $ filter possible input

task2 input = length $ filter possible $ transform input

main = interact $ show . task2 . parse
