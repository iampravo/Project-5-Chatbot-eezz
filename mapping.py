from response_generators import greeting_intent, goodbye_intent, esg_rating_response_generator, mcap_response_generator, profile_details_response_generator

intent_activity={'greetings':greeting_intent,
                 'good_bye': goodbye_intent,
                 'esg_with_company': esg_rating_response_generator,
                 'market_cap_with_company' : mcap_response_generator,
                 'person_profile_with_name' : profile_details_response_generator
                 }
