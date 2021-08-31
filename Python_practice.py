# start
# print('Paul says Hello World')

# # data types
# print(type(3))
# print(type(2019))
# print(type(73.89))
# print(type('Hello World'))
# print(type(''))
# print(type(True))

# declared variables
# snake case and lowercase naming conventions
# num_candidates = 3
# winning_percentage = 73.81
# candidate = 'Diane'
# won_election = True

# Skill Drill
# print(5 + 2 * 3)
# print(8 // 5 - 3)
# print(8 + 22 * 2 - 4)
# print(16 - 3 / 2 + 7 - 1)
# print(3 ** 3 % 5)
# print(5 + 9 * 3 / 2 - 4)
# print('---------------------')
# print((5 + 2) * 3)
# print((8 // 5) - 3)
# print(8 + (22 * (2 - 4)))
# print(16 - 3 / (2 + 7) - 1)
# print(3 ** (3 % 5))
# print('----------------------')
# print(5 + (9 * 3 / 2 - 4))
# print(5 + (9 * 3 / (2 - 4)))
# print('----------------------')
# counties = ['Arapahoe', 'Denver', 'Jefferson']
# counties.insert(1, 'El Paso')
# counties.pop(0)
# counties.pop()
# counties.insert(1, 'Jefferson')
# counties.append('Arapahoe')
# print(counties)
# print('----------------------')
# counties_tuple = ('Arapahoe','Denver','Jefferson')
# print(counties_tuple[:-2])
# print(counties_tuple[:2])
# print(counties_tuple[:-1])
# print(counties_tuple[1:2])
# print('----------------------')
# voting_data = []
# voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
# voting_data.append({'county':'Denver', 'registered_voters': 463353})
# voting_data.append({'county':'Jefferson', 'registered_voters': 432438})
# voting_data.insert(1, {'county': 'El Paso', 'registered_voters': 461149})
# voting_data.pop(0)
# print('----------------------')
# # How many votes did you get?
# my_votes = int(input('How many votes did you get in the election? '))
# #  Total votes in the election
# total_votes = int(input('What is the total votes in the election? '))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print('I received ' + str(percentage_votes)+'% of the total votes.')
# print('----------------------')
# counties = ['Arapahoe','Denver','Jefferson']
# if 'El Paso' in counties:
#     print('El Paso is in the list of counties.')
# else:
#     print('El Paso is not the list of counties.')
# print('----------------------')
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
print('----------------------')
voting_data = [
    {'county':'Arapahoe', 'registered_voters': 422829},
    {'county':'Denver', 'registered_voters': 463353},
    {'county':'Jefferson', 'registered_voters': 432438}]
for data_point in voting_data:
    county = data_point.get('county')
    voters = data_point.get('registered_voters')
    print(f'{county} county has {voters:{6},.0f} registered voters.')