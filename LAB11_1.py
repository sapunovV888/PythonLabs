import pandas as pd

classmates={'Sapunov':(186,'boy'), 'Petrushanko': (192,'boy'),'Naumenko':( 182,'boy'),'Buryak':(178,'girl'),'Pushkar':(180,'girl'),'Galuga':(188,'boy'),'Marinchenko':(178,'boy'),'Koval':(174,'girl'),'Dudarenko':(190,'boy'),'Shapoval':(170,'girl')}

class_height = pd.DataFrame.from_dict(classmates, orient='index', columns=['Height','Gender'])
print('Classmates Height')
print(class_height)
class_height_mean=(class_height.groupby('Gender').mean())
class_height_mean.rename(columns={'Height':'Average_height'}, inplace=True)
class_height_mean['Sum_height']=True
class_height_mean['Sum_height']=class_height.groupby('Gender').sum()['Height']
print('\nMean by Height:')
print(class_height_mean)