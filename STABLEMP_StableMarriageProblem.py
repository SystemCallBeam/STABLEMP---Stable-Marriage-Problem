n = int(input())
H = n*[0]
Member = n*[0]
Index = n*[0]

for i in range(n):
  Member[i] = int(input())
  H[i] = (Member[i]*2) * [0]
  Index[i] = Member[i]*[1]
  for j in range(Member[i]*2):
    H[i][j] = [int(x) for x in input().split()]
    H[i][j][0] = 0

def findIdx(ValM_W, Table, i, Midx):
  for idxM_W in range(1, len(Table[i][Midx])):
    if Table[i][Midx][idxM_W] == ValM_W:
      return idxM_W;

def Check(Table, n):
  for i in range(n):
    for no in range(len(Table[i])):
      if Table[i][no][0] == 0:
        return True
  else:
    return False

E_noCouple = True
while E_noCouple:

  for i in range(n):

    k = Member[i]
    for j in range(k):

      if H[i][j + k][0] != 0 or Index[i][j] > k:
        continue  

      Midx = H[i][j + k][Index[i][j]] - 1
      idxM_W = H[i][Midx][0]
      Widx = H[i][Midx][idxM_W] - 1
      ValW_M = H[i][Widx + k][0]

      if H[i][Midx][0] == 0:   # ถ้ายังไม่มีคู่
        H[i][Midx][0] = findIdx(j + 1, H, i, Midx)
        H[i][j + k][0] = Midx + 1
        H[i][j + k][Index[i][j]] = 0
        Index[i][j]+=1
      else:  # ถ้ามีคู่แล้ว
        idx = findIdx(j + 1, H, i, Midx)
        if idx < idxM_W:  # ถ้าผู้หญิงชอบผู้ชายคนนี้มากกว่าคนเก่า
          H[i][Widx + k][0] = 0
          H[i][Midx][0] = findIdx(j + 1, H, i, Midx)
          H[i][j + k][0] = Midx + 1
          H[i][j + k][Index[i][j]] = 0
          Index[i][j]+=1
        else:
          H[i][j + k][Index[i][j]] = 0
          Index[i][j]+=1
    E_noCouple = Check(H, n)

for i in range(n):
  for j in range(Member[i]):
    print(j + 1, H[i][j + Member[i]][0])