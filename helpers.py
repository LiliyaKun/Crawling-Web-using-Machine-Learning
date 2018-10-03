"""
Functions for using in the construction of datasets

"""


import re



def getText(parent):
   return ''.join(parent.find_all(text=True, recursive=False)).strip()



def getChildText(df_raw_features, tag_list, tag_text_list):
   i = 0
   for tag in tag_list:
       childtext = []

       for child in tag.find_all(recursive=False):

           if child.name in tag_text_list:
               childtext.append(getText(child))

       if len(''.join(childtext)) > 0 and df_raw_features.loc[:,'num_child_elements'][i] > 0:
           df_raw_features.loc[:,'child_text'][i] = ''.join(childtext)

       else:
           df_raw_features.loc[:,'child_text'][i] = 'CEML_NO_TEXT'
       i += 1




def is_thumbnail(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:

       if tag.name == 'img':

           if tag.parent.name == 'a' and len(tag.parent.find_all(recursive=False)) == 1:

               df_derived_features.loc[:,'is_thumbnail'][i] = 1
               i += 1

           elif tag.parent.name == 'a' and len(tag.parent.find_all(recursive=False)) > 1:

               df_derived_features.loc[:,'is_thumbnail'][i] = 0
               i += 1

           else:
               i += 1
       else:
           i += 1




def is_link(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       childlist = []

       for child in tag.find_all(recursive=False):
           childlist.append(child.name)

       if "a" in childlist and len(childlist) == 1:
           df_derived_features.loc[:,'is_link'][i] = 1
           i += 1

       else:
           df_derived_features.loc[:,'is_link'][i] = 0
           i += 1




def is_sib_p(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:

       if tag.name == 'p':

           if len(tag.parent.find_all(recursive=False)) > 1:
               df_derived_features.loc[:,'is_sib_p'][i] = 1
               i += 1

           else:
               df_derived_features.loc[:,'is_sib_p'][i] = 0
               i += 1
       else:
           df_derived_features.loc[:,'is_sib_p'][i] = 0
           i += 1




def is_sib_a(tag_list, df_derived_features):
   i=0
   for tag in tag_list:

        if tag.name == 'a':

              if len(tag.parent.find_all(recursive=False)) > 1:
                 df_derived_features.loc[:,'is_sib_a'][i] = 1
                 i += 1

              else:
                 df_derived_features.loc[:,'is_sib_a'][i] = 0
                 i += 1
        else:
            df_derived_features.loc[:,'is_sib_a'][i] = 0
            i += 1




def is_sib_input(tag_list, df_derived_features):
   i=0
   for tag in tag_list:

        if tag.name == 'input':

              if len(tag.parent.find_all(recursive=False)) > 1:
                 df_derived_features.loc[:,'is_sib_input'][i] = 1
                 i += 1

              else:
                 df_derived_features.loc[:,'is_sib_input'][i] = 0
                 i += 1
        else:
            df_derived_features.loc[:,'is_sib_input'][i] = 0
            i += 1




def is_desc_nav(tag_list, df_derived_features):
   i=0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_nav'][i] = 0

       if (tag.has_attr('id') and "nav" in ''.join(tag.get('id')).lower()) or (tag.has_attr('class') and "nav" in ''.join(tag.get('class')).lower()):
           df_derived_features.loc[:,'is_desc_nav'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and "nav" in ''.join(parent.get('id')).lower()) or (parent.has_attr('class') and "nav" in ''.join(parent.get('class')).lower()):
                  df_derived_features.loc[:,'is_desc_nav'][i] = 1
                  break

               else:
                  parent = parent.parent
       i += 1




def is_desc_comment(tag_list, df_derived_features):
   i=0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_comment'][i] = 0

       if (tag.has_attr('id') and "comment" in ''.join(tag.get('id')).lower()) or (tag.has_attr('class') and "comment" in ''.join(tag.get('class')).lower()):
           df_derived_features.loc[:,'is_desc_comment'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and "comment" in ''.join(parent.get('id')).lower()) or (parent.has_attr('class') and "comment" in ''.join(parent.get('class')).lower()):
                  df_derived_features.loc[:,'is_desc_comment'][i] = 1
                  break

               else:
                  parent = parent.parent
       i += 1




def is_desc_main(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features['is_desc_main'][i] = 0

       if (tag.has_attr('id') and "main" in ''.join(tag.get('id')).lower()) or (tag.has_attr('class') and "main" in ''.join(tag.get('class')).lower()):
           df_derived_features.loc[:,'is_desc_main'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and "main" in ''.join(parent.get('id')).lower()) or (parent.has_attr('class') and "main" in ''.join(parent.get('class')).lower()):
                   df_derived_features.loc[:,'is_desc_main'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_footer(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_footer'][i] = 0

       if (tag.has_attr('id') and "footer" in ''.join(tag.get('id')).lower()) or (tag.has_attr('class') and "footer" in ''.join(tag.get('class')).lower()):
           df_derived_features.loc[:,'is_desc_footer'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and "footer" in ''.join(parent.get('id')).lower()) or (parent.has_attr('class') and "footer" in ''.join(parent.get('class')).lower()):
                   df_derived_features.loc[:,'is_desc_footer'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_wrapper(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_wrapper'][i] = 0

       if (tag.has_attr('id') and "wrapper" in ''.join(tag.get('id')).lower()) or (tag.has_attr('class') and "wrapper" in ''.join(tag.get('class')).lower()):
           df_derived_features.loc[:,'is_desc_wrapper'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and "wrapper" in ''.join(parent.get('id')).lower()) or (parent.has_attr('class') and "wrapper" in ''.join(parent.get('class')).lower()):
                   df_derived_features.loc[:,'is_desc_wrapper'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_aside(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_aside'][i] = 0

       if (tag.has_attr('id') and "aside" in ''.join(tag.get('id')).lower()) or (tag.has_attr('class') and "aside" in ''.join(tag.get('class')).lower()):
           df_derived_features.loc[:,'is_desc_aside'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and "aside" in ''.join(parent.get('id')).lower()) or (parent.has_attr('class') and "aside" in ''.join(parent.get('class')).lower()):
                   df_derived_features.loc[:,'is_desc_aside'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_ad(tag_list, df_derived_features, regex_ad):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_ad'][i] = 0

       if (tag.has_attr('id') and bool(re.search(regex_ad, ''.join(tag.get('id')).lower()))) or (tag.has_attr('class') and bool(re.search(regex_ad, ''.join(tag.get('class')).lower()))):
           df_derived_features.loc[:,'is_desc_ad'][i] = 1

       else:
           while parent is not None:

               if (parent.has_attr('id') and bool(re.search(regex_ad, ''.join(parent.get('id')).lower()))) or (parent.has_attr('class') and bool(re.search(regex_ad, ''.join(parent.get('class')).lower()))):
                   df_derived_features.loc[:,'is_desc_ad'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1



def get_contains_column(df_derived_features, df_raw_features, list_row_count, elem_contains):
    """
    Check if the inner text of the node contains same text like 'rights reserved','like' or 'share'

    and save his boolean values in column 'contains_rights_reserved'

    """
    if elem_contains == "rights reserved":
       df_derived_features.loc[:,'contains_rights_reserved'] = [1 if elem_contains in df_raw_features.loc[:,'inner_text'][i].lower() else 0 for i in list_row_count]

    if elem_contains == "like":
       df_derived_features.loc[:,'contains_like'] = [1 if elem_contains in df_raw_features.loc[:,'inner_text'][i].lower() else 0 for i in list_row_count]

    if elem_contains == "share":
       df_derived_features.loc[:,'contains_share'] = [1 if elem_contains in df_raw_features.loc[:,'inner_text'][i].lower() else 0 for i in list_row_count]



def get_class_y(df_derived_features, list_row_count):


   for i in list_row_count:

       if "CEML__TITLE" in df_derived_features.loc[:,'class_name'][i]:
           df_derived_features.loc[:,'y'][i] = 'CEML__TITLE'

       elif 'CEML__PRICE' in df_derived_features.loc[:,'class_name'][i]:
           df_derived_features.loc[:,'y'][i] = 'CEML__PRICE'

       elif 'CEML__URL__IMAGE' in df_derived_features.loc[:,'class_name'][i]:
           df_derived_features.loc[:,'y'][i] = 'CEML__URL__IMAGE'

       elif 'CEML__DESCRIPTION' in df_derived_features.loc[:,'class_name'][i]:
           df_derived_features.loc[:,'y'][i] = 'CEML__DESCRIPTION'

       elif 'CEML__PAGE__DESCRIPTION__LIST__ITEMS' in df_derived_features.loc[:,'class_name'][i]:
           df_derived_features.loc[:,'y'][i] = 'CEML__PAGE__DESCRIPTION__LIST__ITEMS'

       else:
           df_derived_features.loc[:,'y'][i] = 'NOISY'




def is_desc_p(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_p'][i] = 0

       if tag.name == 'p':
           df_derived_features.loc[:,'is_desc_p'][i] = 1

       else:
           while parent is not None:

               if parent.name == 'p':
                   df_derived_features.loc[:,'is_desc_p'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_div(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_div'][i] = 0

       if tag.name == 'div':
           df_derived_features.loc[:,'is_desc_div'][i] = 1

       else:
           while parent is not None:

               if parent.name == 'div':
                   df_derived_features.loc[:,'is_desc_div'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_ul(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_ul'][i] = 0

       if tag.name == 'ul':
           df_derived_features.loc[:,'is_desc_ul'][i] = 1

       else:
           while parent is not None:

               if parent.name == 'ul':
                   df_derived_features.loc[:,'is_desc_ul'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_table(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_table'][i] = 0

       if tag.name == 'table':
           df_derived_features.loc[:,'is_desc_table'][i] = 1

       else:
           while parent is not None:

               if parent.name == 'table':
                   df_derived_features.loc[:,'is_desc_table'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_h(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_h'][i] = 0

       if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
           df_derived_features.loc[:,'is_desc_h'][i] = 1

       else:
           while parent is not None:

               if parent.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                   df_derived_features.loc[:,'is_desc_h'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_ol(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_ol'][i] = 0

       if tag.name == 'ol':
           df_derived_features.loc[:,'is_desc_ol'][i] = 1

       else:
           while parent is not None:

               if parent.name == 'ol':
                   df_derived_features.loc[:,'is_desc_ol'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def is_desc_menu(tag_list, df_derived_features):
   i = 0
   for tag in tag_list:
       parent = tag.parent
       df_derived_features.loc[:,'is_desc_menu'][i] = 0

       if tag.name == 'menu':
           df_derived_features.loc[:,'is_desc_menu'][i] = 1

       else:
           while parent is not None:

               if parent.name == 'menu':
                   df_derived_features.loc[:,'is_desc_menu'][i] = 1
                   break

               else:
                   parent = parent.parent
       i += 1




def has_depth_greater_2(tag_list, df_derived_features):
   do_break = False
   i = 0
   for tag in tag_list:
      if do_break:
         do_break = False

      if tag.name in ['div','table','ol','ul','menu']:

         children1 = tag.find_all(recursive=False)
         if len(children1) > 0:

             for child_level1 in children1:
                 if do_break:
                    break

                 children2 = child_level1.find_all(recursive=False)

                 if len(children2) > 0:

                     for child_level2 in children2:
                         children3 = child_level2.find_all(recursive=False)

                         if len(children3) > 0:
                            df_derived_features.loc[:,'has_depth_greater_2'][i] = True
                            i += 1
                            do_break = True
                            break

             if not do_break:
                df_derived_features.loc[:,'has_depth_greater_2'][i] = False
                i += 1
         else:
             df_derived_features.loc[:,'has_depth_greater_2'][i] = False
             i += 1
      else:
          df_derived_features.loc[:,'has_depth_greater_2'][i] = False
          i += 1







