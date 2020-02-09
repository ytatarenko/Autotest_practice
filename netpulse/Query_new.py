chains=[
'5180bb25-7e1e-4260-8cfc-693758c6e69e',
'fbe85349-4827-4680-813c-aeb218fb63b9',
'48559b88-6835-4d1c-9771-d166c5792cdb'
]

chain='fbe85349-4827-4680-813c-aeb218fb63b9'

preference_set_ids=[
3301,
3302,
3303,
3304,
3305,
3306,
3308,
3309,
3310,
3311,
3312,
3313,
3314,
3315,
3316,
3317,
3318,
3319,
3319,
3320,
3321,
3322,
3323,
3324,
3325,
3326,
3327,
3328,
3329,
3330,
3331,
3332,
3333,
3334,
3335,
3337,
3338,
3339,
3341,
3342,
3343,
3344,
3345,
3346,
3347,
3348,
3349,
3351,
3352,
3353,
3354,
3355,
3356,
3357,
3358,
3359,
3360,
3361,
3362,
3363,
3364,
3365,
3367,
3368
]




for i in range(0, len(preference_set_ids)):
    print ('set @preference_set_id='+str(preference_set_ids[i])+'; '
            'set @feature_id=(select id from feature where gym_chain_id=\''+chain+'\' and type =\'deals\');'
            'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
            'set @id=LAST_INSERT_ID();'
            'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-deals.png"\', @id); '
            )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'challenges\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-challenges.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'findAClass\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-find-a-class.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'goalCenter\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-goal-centre.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'referAFriendAdvanced\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-refer-a-friend.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'rewardsExtended\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-rewards.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'myAccount\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-my-account.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'social\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-activity-feed.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'recordWorkout\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-record-a-workout.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'workouts\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-workouts.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'advancedWorkouts\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-workouts.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and type =\'requestTrainer\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-training.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and name =\'SwimTimetable\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-find-a-class.png"\', @id); '
          )
    print('set @preference_set_id=' + str(preference_set_ids[i]) + '; '
                                                                   'set @feature_id=(select id from feature where gym_chain_id=\'' + chain + '\' and name =\'BookAnActivity\');'
                                                                                                                                             'INSERT INTO `feature_preference` (`id`, `name`, `feature_id`, `preference_set_id`) VALUES (NULL, \'iconUrl\', @feature_id, @preference_set_id); '
                                                                                                                                             'set @id=LAST_INSERT_ID();'
                                                                                                                                             'INSERT INTO `feature_preference_value_item` (`id`, `key`, `value`, `feature_preference_id`) VALUES (NULL, NULL, \'"/img/customicons/dashboard/LCC_ic-find-a-class.png"\', @id); '
          )