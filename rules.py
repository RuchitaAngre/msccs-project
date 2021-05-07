def findDecision(obj): #obj[0]: Quality, obj[1]: Quantity, obj[2]: Cheaper in price, obj[3]: Satisfaction, obj[4]: Has  COVID-19   increased time you spent online  grocery Shopping    ? , obj[5]: How often do you shop online in last six month?, obj[6]: Overall Experience
   # {"feature": "Satisfaction", "instances": 370, "metric_value": 30.021, "depth": 1}
   if obj[3] == '>0':
      # {"feature": "Overall Experience", "instances": 265, "metric_value": 25.1036, "depth": 2}
      if obj[6]<=4:
         # {"feature": "How often do you shop online in last six month?", "instances": 153, "metric_value": 14.9732, "depth": 3}
         if obj[5]<=2:
            # {"feature": "Quality", "instances": 97, "metric_value": 10.3669, "depth": 4}
            if obj[0] == 'Yes':
               # {"feature": "Cheaper in price", "instances": 86, "metric_value": 10.2348, "depth": 5}
               if obj[2] == 'Yes':
                  # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 70, "metric_value": 9.8221, "depth": 6}
                  if obj[4]>0:
                     # {"feature": "Quantity", "instances": 60, "metric_value": 9.5334, "depth": 7}
                     if obj[1] == 'Yes':
                        return 'Yes'
                     elif obj[1] == 'No':
                        return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[4]<=0:
                     # {"feature": "Quantity", "instances": 10, "metric_value": 2.0, "depth": 7}
                     if obj[1] == 'Yes':
                        return 'Yes'
                     elif obj[1] == 'No':
                        return 'Yes'
                     else:
                        return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'No':
                  # {"feature": "Quantity", "instances": 16, "metric_value": 2.9436, "depth": 6}
                  if obj[1] == 'Yes':
                     # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 10, "metric_value": 2.8284, "depth": 7}
                     if obj[4]>0:
                        return 'Yes'
                     elif obj[4]<=0:
                        return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[1] == 'No':
                     # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 6, "metric_value": 3.266, "depth": 7}
                     if obj[4]>0:
                        return 'Yes'
                     elif obj[4]<=0:
                        return 'No'
                     else:
                        return 'No'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[0] == 'No':
               # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 11, "metric_value": 5.2998, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Quantity", "instances": 9, "metric_value": 4.7589, "depth": 6}
                  if obj[1] == 'Yes':
                     # {"feature": "Cheaper in price", "instances": 6, "metric_value": 2.8284, "depth": 7}
                     if obj[2] == 'Yes':
                        return 'No'
                     elif obj[2] == 'No':
                        return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[1] == 'No':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4]<=0:
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[5]>2:
            # {"feature": "Quality", "instances": 56, "metric_value": 9.165, "depth": 4}
            if obj[0] == 'Yes':
               # {"feature": "Quantity", "instances": 48, "metric_value": 9.4593, "depth": 5}
               if obj[1] == 'Yes':
                  # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 47, "metric_value": 9.7548, "depth": 6}
                  if obj[4]>0:
                     # {"feature": "Cheaper in price", "instances": 46, "metric_value": 10.1016, "depth": 7}
                     if obj[2] == 'Yes':
                        return 'Yes'
                     elif obj[2] == 'No':
                        return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[4]<=0:
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'No':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[0] == 'No':
               # {"feature": "Quantity", "instances": 8, "metric_value": 3.0178, "depth": 5}
               if obj[1] == 'Yes':
                  # {"feature": "Cheaper in price", "instances": 7, "metric_value": 3.7236, "depth": 6}
                  if obj[2] == 'Yes':
                     # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 6, "metric_value": 3.3116, "depth": 7}
                     if obj[4]>0:
                        return 'Yes'
                     elif obj[4]<=0:
                        return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[2] == 'No':
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'No':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[6]>4:
         # {"feature": "How often do you shop online in last six month?", "instances": 112, "metric_value": 20.6805, "depth": 3}
         if obj[5]<=2:
            # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 69, "metric_value": 14.1224, "depth": 4}
            if obj[4]>0:
               # {"feature": "Cheaper in price", "instances": 64, "metric_value": 13.4177, "depth": 5}
               if obj[2] == 'Yes':
                  # {"feature": "Quality", "instances": 60, "metric_value": 10.5893, "depth": 6}
                  if obj[0] == 'Yes':
                     # {"feature": "Quantity", "instances": 60, "metric_value": 10.5893, "depth": 7}
                     if obj[1] == 'Yes':
                        return 'Yes'
                     else:
                        return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'No':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[4]<=0:
               return 'Yes'
            else:
               return 'Yes'
         elif obj[5]>2:
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == '<=0':
      # {"feature": "Cheaper in price", "instances": 105, "metric_value": 17.6783, "depth": 2}
      if obj[2] == 'Yes':
         # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 62, "metric_value": 13.4565, "depth": 3}
         if obj[4]>0:
            # {"feature": "How often do you shop online in last six month?", "instances": 48, "metric_value": 11.3266, "depth": 4}
            if obj[5]<=2:
               # {"feature": "Overall Experience", "instances": 34, "metric_value": 9.1017, "depth": 5}
               if obj[6]>1:
                  # {"feature": "Quantity", "instances": 26, "metric_value": 8.1881, "depth": 6}
                  if obj[1] == 'No':
                     # {"feature": "Quality", "instances": 19, "metric_value": 6.4734, "depth": 7}
                     if obj[0] == 'No':
                        return 'No'
                     elif obj[0] == 'Yes':
                        return 'No'
                     else:
                        return 'No'
                  elif obj[1] == 'Yes':
                     # {"feature": "Quality", "instances": 7, "metric_value": 4.8783, "depth": 7}
                     if obj[0] == 'No':
                        return 'No'
                     elif obj[0] == 'Yes':
                        return 'Yes'
                     else:
                        return 'Yes'
                  else:
                     return 'No'
               elif obj[6]<=1:
                  # {"feature": "Quality", "instances": 8, "metric_value": 5.1559, "depth": 6}
                  if obj[0] == 'No':
                     return 'No'
                  elif obj[0] == 'Yes':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'No'
            elif obj[5]>2:
               # {"feature": "Overall Experience", "instances": 14, "metric_value": 6.5132, "depth": 5}
               if obj[6]<=3:
                  return 'No'
               elif obj[6]>3:
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[4]<=0:
            return 'No'
         else:
            return 'No'
      elif obj[2] == 'No':
         # {"feature": "Overall Experience", "instances": 43, "metric_value": 11.3723, "depth": 3}
         if obj[6]>1:
            # {"feature": "Quantity", "instances": 27, "metric_value": 8.0991, "depth": 4}
            if obj[1] == 'No':
               # {"feature": "Has  COVID-19   increased time you spent online  grocery Shopping    ? ", "instances": 15, "metric_value": 5.8132, "depth": 5}
               if obj[4]>0:
                  # {"feature": "How often do you shop online in last six month?", "instances": 11, "metric_value": 4.357, "depth": 6}
                  if obj[5]>1:
                     # {"feature": "Quality", "instances": 9, "metric_value": 3.3116, "depth": 7}
                     if obj[0] == 'No':
                        return 'No'
                     elif obj[0] == 'Yes':
                        return 'No'
                     else:
                        return 'No'
                  elif obj[5]<=1:
                     return 'No'
                  else:
                     return 'No'
               elif obj[4]<=0:
                  return 'No'
               else:
                  return 'No'
            elif obj[1] == 'Yes':
               # {"feature": "Quality", "instances": 12, "metric_value": 6.1046, "depth": 5}
               if obj[0] == 'No':
                  return 'No'
               elif obj[0] == 'Yes':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[6]<=1:
            return 'No'
         else:
            return 'No'
      else:
         return 'No'
   else:
      return 'No'
