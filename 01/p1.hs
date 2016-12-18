import qualified Data.Set as S

input = [L 2, L 3, L 3, L 4, R 1, R 2, L 3, R 3, R 3, L 1, L 3, R 2, R 3, L 3, R 4, R 3, R 3, L 1, L 4, R 4, L 2, R 5, R 1, L 5, R 1, R 3, L 5, R 2, L 2, R 2, R 1, L 1, L 3, L 3, R 4, R 5, R 4, L 1, L 189, L 2, R 2, L 5, R 5, R 45, L 3, R 4, R 77, L 1, R 1, R 194, R 2, L 5, L 3, L 2, L 1, R 5, L 3, L 3, L 5, L 5, L 5, R 2, L 1, L 2, L 3, R 2, R 5, R 4, L 2, R 3, R 5, L 2, L 2, R 3, L 3, L 2, L 1, L 3, R 5, R 4, R 3, R 2, L 1, R 2, L 5, R 4, L 5, L 4, R 4, L 2, R 5, L 3, L 2, R 4, L 1, L 2, R 2, R 3, L 2, L 5, R 1, R 1, R 3, R 4, R 1, R 2, R 4, R 5, L 3, L 5, L 3, L 3, R 5, R 4, R 1, L 3, R 1, L 3, R 3, R 3, R 3, L 1, R 3, R 4, L 5, L 3, L 1, L 5, L 4, R 4, R 1, L 4, R 3, R 3, R 5, R 4, R 3, R 3, L 1, L 2, R 1, L 4, L 4, L 3, L 4, L 3, L 5, R 2, R 4, L 2]

data Dir = N | E | S | W deriving (Show)
data Pos = Pos Dir Int Int deriving (Show)
data Step = L Int | R Int deriving (Show)

right :: Dir -> Dir
right N = E
right E = S
right S = W
right W = N

left :: Dir -> Dir
left dir = right $ right $ right dir

step :: Int -> Pos -> Pos
step steps (Pos N n e) = Pos N (n+steps) e
step steps (Pos E n e) = Pos E n (e+steps)
step steps (Pos S n e) = Pos S (n-steps) e
step steps (Pos W n e) = Pos W n (e-steps)

walk :: Pos -> Step -> Pos
walk (Pos dir n e) (R steps) = step steps $ Pos (right dir) n e
walk (Pos dir n e) (L steps) = step steps $ Pos (left dir) n e

expand :: Int -> Int -> [Int]
expand a b
  | a <= b = [a .. b]
  | otherwise = reverse [b .. a]

interp :: Pos -> Pos -> [Pos]
interp (Pos _ n1 e1) (Pos N n2 e2) = tail $ zipWith (Pos N) (expand n1 n2) (repeat e1)
interp (Pos _ n1 e1) (Pos E n2 e2) = tail $ zipWith (Pos E) (repeat n1) (expand e1 e2)
interp (Pos _ n1 e1) (Pos S n2 e2) = tail $ zipWith (Pos S) (expand n1 n2) (repeat e1)
interp (Pos _ n1 e1) (Pos W n2 e2) = tail $ zipWith (Pos W) (repeat n1) (expand e1 e2)

walk_list :: Pos -> [Step] -> [Pos]
walk_list p (s:[]) = interp p $ walk p s
walk_list p (s:ss) = (interp p nextleap) ++ (walk_list nextleap ss)
  where nextleap = walk p s

memo_walk :: S.Set (Int, Int) -> [Pos] -> Pos
memo_walk set (p:[]) = p
memo_walk set ((Pos dir n e):ps)
  | S.member (n, e) set = Pos dir n e
  | otherwise    = memo_walk (S.insert (n, e) set) ps

distance (Pos _ n e) = (abs n) + (abs e)

part1 = print $ distance $ foldl walk (Pos N 0 0) input

part2 = print $ distance $ memo_walk S.empty $ walk_list (Pos N 0 0) input

main = part2

