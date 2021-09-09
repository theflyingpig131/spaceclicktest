import json, time, random



def main():
  data = json.loads(open("attempts.json", "r").read())


  def sort_cey(daddy):
      return daddy["Score"]
  data.sort(key=sort_cey, reverse=True)

  current = 1

  for x in (data):
    print(" #%s  | %s | %s"%(current,x["Name"], x["Score"]))
    current += 1