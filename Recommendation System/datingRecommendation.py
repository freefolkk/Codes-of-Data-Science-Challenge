import numpy
from lightfm import LightFM
from ratingsData import fetch_ratings 


#fetch dataset using our own method fetch_data
data = fetch_ratings()

#creating a model using LightFM class off lightfm module
model = LightFM(loss='warp') 
model.fit(data['ratings'], epochs=30, num_threads=2)

def recommend_match(model, data, user_ids):
	n_user, n_matches = data['ratings'].shape

	for user_id in user_ids:

		scores = model.predict(user_id, numpy.arange(n_matches))
		topScores = numpy.argsort(-scores)[:3]

		print('recommendation for user : %s' % user_id)

		for x in topScores[:3]:
			print("    %s"%x)

recommend_match(model, data, [1])			